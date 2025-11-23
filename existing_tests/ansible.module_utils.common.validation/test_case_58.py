import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_59(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'I[9\t^n!s#\x0cm'
        list_0 = [str_0, str_0, str_0, str_0]
        dict_0 = {}
        var_0 = module_0.check_required_together(str_0, list_0, dict_0)

if __name__ == "__main__":
    unittest.main()
