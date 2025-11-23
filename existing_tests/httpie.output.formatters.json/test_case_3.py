import unittest
import timeout_decorator
import httpie.output.formatters.json as module_0
import json as module_1

class Test_Json_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            j_s_o_n_formatter_0 = module_0.JSONFormatter()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
