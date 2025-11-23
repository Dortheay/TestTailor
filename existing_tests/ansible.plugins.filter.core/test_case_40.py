import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_41(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_40(self):
        try:
            str_0 = 'W,YT^&CAvZAN@/'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
            list_0 = [dict_0, dict_0, str_0, str_0]
            dict_1 = {str_0: str_0, str_0: str_0}
            var_0 = module_0.subelements(list_0, dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
