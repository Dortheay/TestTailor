import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = 'Q^pyF\t2'
            var_0 = module_0.check_type_int(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
