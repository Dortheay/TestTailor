import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_68(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        list_0 = []
        tuple_0 = None
        var_0 = module_0.check_required_if(list_0, tuple_0)
        str_0 = None
        set_0 = set()
        var_1 = module_0.check_mutually_exclusive(str_0, set_0, tuple_0)

if __name__ == "__main__":
    unittest.main()
