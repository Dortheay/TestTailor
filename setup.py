from setuptools import setup, find_packages

setup(
    name="testtailor",
    version="0.1.0",
    description="Generating High-Coverage Tests via Path-Proximal Tests with LLMs",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "openai>=1.0.0",
        "coverage>=7.0",
    ],
    entry_points={
        "console_scripts": [
            "testtailor=testtailor.main:main",
        ]
    },
)