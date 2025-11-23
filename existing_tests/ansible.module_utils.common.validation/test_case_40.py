import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_41(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_40(self):
        try:
            bytes_0 = b'\x94t\x06\xf4\xac'
            dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
            set_0 = set()
            bool_0 = True
            var_0 = module_0.check_mutually_exclusive(set_0, bool_0)
            bytes_1 = b'\x10\xbd\xabf\\Q\x83\x1a\x95'
            var_1 = module_0.check_required_arguments(dict_0, bytes_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
