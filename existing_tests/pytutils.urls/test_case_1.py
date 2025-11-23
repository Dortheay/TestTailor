import unittest
import timeout_decorator
import pytutils.urls as module_0

class Test_Urls_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'Cng-D'
            var_0 = module_0.update_query_params(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
