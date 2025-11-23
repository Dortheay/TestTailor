import unittest
import timeout_decorator
import httpie.output.formatters.json as module_0
import json as module_1

class Test_Json_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'json'
        str_1 = 'format'
        str_2 = 'sort_keys'
        str_3 = '\x0cn4nt'
        bool_0 = True
        int_0 = 4
        var_0 = {str_1: bool_0, str_2: bool_0, str_3: int_0}
        var_1 = {str_0: var_0}
        str_4 = 'explicit_json'
        str_5 = 'format_options'
        bool_1 = False
        var_2 = {str_4: bool_1, str_5: var_1}
        j_s_o_n_formatter_0 = module_0.JSONFormatter(**var_2)
        str_6 = 'name'
        str_7 = 'value'
        str_8 = 'u~=est'
        int_1 = 42
        var_3 = {str_6: str_8, str_7: int_1}
        var_4 = var_1[str_0][str_2]
        var_5 = var_1[str_0][str_3]
        var_6 = module_1.dumps(var_3, ensure_ascii=bool_1, indent=var_5, sort_keys=var_4)
        str_9 = '7_NVTtaENAW'
        str_10 = j_s_o_n_formatter_0.format_body(str_9, str_7)

if __name__ == "__main__":
    unittest.main()
