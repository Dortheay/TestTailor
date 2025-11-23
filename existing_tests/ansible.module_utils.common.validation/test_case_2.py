import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '}O&S'
            bytes_0 = b'\x8a\xbd\xc4\xe5\xf9\xafX'
            var_0 = module_0.check_required_one_of(str_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
