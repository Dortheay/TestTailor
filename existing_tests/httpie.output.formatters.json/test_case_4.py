import unittest
import timeout_decorator
import httpie.output.formatters.json as module_0
import json as module_1

class Test_Json_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'json'
            str_1 = 'format'
            str_2 = 'sort_keys'
            str_3 = 'indent'
            bool_0 = True
            int_0 = 4
            var_0 = {str_1: bool_0, str_2: bool_0, str_3: int_0}
            var_1 = {str_0: var_0}
            str_4 = 'format_options'
            var_2 = {str_4: var_1, str_4: bool_0}
            j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
