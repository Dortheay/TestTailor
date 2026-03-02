"""
LLM Client
==========
Thin wrapper around the OpenAI-compatible chat completion API.
Supports GPT-4o and DeepSeek-V3 (which is OpenAI-API-compatible).
"""

import re
import time
from dataclasses import dataclass
from typing import Optional

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

from config import TestTailorConfig


@dataclass
class LLMResponse:
    content: str
    prompt_tokens: int = 0
    completion_tokens: int = 0
    cost_usd: float = 0.0


# Token pricing ($ per 1 K tokens) – update as prices change
_PRICING = {
    "gpt-4o-2024-11-20":     (0.0025, 0.01),    # (input, output) per 1K tokens
    "deepseek-v3":            (0.00014, 0.00028),
    "deepseek-chat":          (0.00014, 0.00028),
}

_DEEPSEEK_BASE_URL = "https://api.deepseek.com"


class LLMClient:
    """
    Wraps the OpenAI SDK to call either GPT-4o or DeepSeek-V3.
    """

    def __init__(self, config: TestTailorConfig):
        self.config = config
        if not OPENAI_AVAILABLE:
            raise RuntimeError(
                "openai package not installed. Run: pip install openai"
            )
        # Build client
        kwargs = {"api_key": config.api_key or "sk-placeholder"}
        if config.api_base:
            kwargs["base_url"] = config.api_base
        elif "deepseek" in config.llm_model.lower():
            kwargs["base_url"] = _DEEPSEEK_BASE_URL

        self._client = OpenAI(**kwargs)
        self._call_count = 0
        self._total_cost = 0.0

    # ── Public API ──────────────────────────────────────────────────────────

    def complete(self, prompt: str, system: str = "") -> LLMResponse:
        """
        Send a prompt and return an LLMResponse.
        Retries once on transient errors.
        """
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        for attempt in range(2):
            try:
                resp = self._client.chat.completions.create(
                    model=self.config.llm_model,
                    messages=messages,
                    temperature=self.config.llm_temperature,
                    max_tokens=self.config.llm_max_tokens,
                )
                self._call_count += 1
                content = resp.choices[0].message.content or ""
                in_tok = resp.usage.prompt_tokens if resp.usage else 0
                out_tok = resp.usage.completion_tokens if resp.usage else 0
                cost = self._estimate_cost(in_tok, out_tok)
                self._total_cost += cost
                return LLMResponse(
                    content=content,
                    prompt_tokens=in_tok,
                    completion_tokens=out_tok,
                    cost_usd=cost,
                )
            except Exception as exc:
                if attempt == 0:
                    time.sleep(2)
                else:
                    raise RuntimeError(f"LLM call failed: {exc}") from exc

    @property
    def total_calls(self) -> int:
        return self._call_count

    @property
    def total_cost_usd(self) -> float:
        return self._total_cost

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _estimate_cost(self, in_tok: int, out_tok: int) -> float:
        model_key = self.config.llm_model
        in_price, out_price = _PRICING.get(model_key, (0.003, 0.006))
        return (in_tok / 1000) * in_price + (out_tok / 1000) * out_price


# ──────────────────────────────────────────────────────────────────────────────
# Response parser
# ──────────────────────────────────────────────────────────────────────────────

def extract_code(response_text: str) -> Optional[str]:
    """
    Extract the Python code block from the LLM response.
    Handles ```python ... ``` and ``` ... ``` delimiters.
    """
    # Match ```python ... ``` or ``` ... ```
    pattern = r"```(?:python)?\s*\n(.*?)```"
    match = re.search(pattern, response_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    # Fallback: return the whole response if it looks like code
    stripped = response_text.strip()
    if stripped.startswith(("import ", "from ", "class ", "def ", "#")):
        return stripped
    return None
