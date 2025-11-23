import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'W,YT^&CAvZAN@/'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
            dict_1 = {}
            var_0 = module_0.regex_escape(dict_0, dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
