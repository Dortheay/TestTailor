import unittest
import timeout_decorator
import ansible.plugins.action.validate_argument_spec as module_0

class Test_Validate_argument_spec_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = 0.001
            bool_0 = True
            int_0 = 2679
            bytes_0 = b'\xd0-\x11\x92\xd5h\xb8\xeb\xb5\x07\xcd\x15\x05"\xc1t\x91\xdc\xc2'
            dict_0 = {bool_0: bool_0, float_0: int_0, bool_0: bytes_0}
            action_module_0 = module_0.ActionModule(float_0, bool_0, dict_0, dict_0, bool_0, dict_0)
            var_0 = action_module_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
