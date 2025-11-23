import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            str_0 = '}7e@Y0\x0c*6<P\tG9!'
            var_0 = module_0.check_type_bytes(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
