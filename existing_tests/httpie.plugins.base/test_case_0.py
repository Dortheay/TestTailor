import unittest
import timeout_decorator
import httpie.plugins.base as module_0

class Test_Base_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'application/json'
        str_1 = '{"key": "value"}'
        str_2 = 'format_options'
        str_3 = 'opton1'
        str_4 = 'value1'
        str_5 = {str_3: str_4}
        str_6 = {str_2: str_5}
        formatter_plugin_0 = module_0.FormatterPlugin(**str_6)
        str_7 = formatter_plugin_0.format_body(str_1, str_0)

if __name__ == "__main__":
    unittest.main()
