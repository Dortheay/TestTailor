import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_58(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        set_0 = set()
        bytes_0 = b'\xd9\x98o\x0e'
        str_0 = ':I\tE8=2*S_FZne\x0b/v'
        var_0 = module_0.check_required_together(set_0, bytes_0, str_0)

if __name__ == "__main__":
    unittest.main()
