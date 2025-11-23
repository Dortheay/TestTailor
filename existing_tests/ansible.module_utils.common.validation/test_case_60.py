import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_61(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        list_0 = []
        tuple_0 = None
        var_0 = module_0.check_required_if(list_0, tuple_0)

if __name__ == "__main__":
    unittest.main()
