import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_33(self):
        try:
            bytes_0 = None
            str_0 = ';q9tav\x0c?n-'
            dict_0 = {bytes_0: str_0, bytes_0: bytes_0, bytes_0: str_0}
            var_0 = module_0.check_required_together(bytes_0, dict_0)
            list_0 = []
            var_1 = module_0.check_type_float(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
