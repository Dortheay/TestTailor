import unittest
import timeout_decorator
import ansible.plugins.filter.urls as module_0

class Test_Urls_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'tE\\| W'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
            var_0 = module_0.do_urlencode(dict_0)
            list_0 = []
            str_1 = '5\teu7\\V.MjIe\r;A\\(8'
            dict_1 = {str_1: str_1}
            filter_module_0 = module_0.FilterModule(*list_0, **dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
