import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            bytes_0 = b'\xc3LN='
            var_0 = module_0.check_type_list(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
