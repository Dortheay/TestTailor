import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bytes_0 = b'5\x12b\xcc\xd7\n\x98\x9f\xafd\xf1/'
            var_0 = module_0.check_required_if(bytes_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
