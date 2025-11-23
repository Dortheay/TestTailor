import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            dict_0 = {}
            str_0 = 'Mandriva'
            dict_1 = {str_0: dict_0}
            bool_0 = False
            var_0 = module_0.set_fallbacks(dict_1, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
