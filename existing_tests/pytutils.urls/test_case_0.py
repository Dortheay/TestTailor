import unittest
import timeout_decorator
import pytutils.urls as module_0

class Test_Urls_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'Zl6?~'
        dict_0 = {}
        var_0 = module_0.update_query_params(str_0, dict_0)

if __name__ == "__main__":
    unittest.main()
