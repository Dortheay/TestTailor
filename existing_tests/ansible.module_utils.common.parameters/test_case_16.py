import unittest
import timeout_decorator
import ansible.module_utils.common.parameters as module_0

class Test_Parameters_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = '>\nH)%L'
            dict_0 = {str_0: str_0}
            dict_1 = {}
            var_0 = module_0.set_fallbacks(dict_0, dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
