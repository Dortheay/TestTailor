import unittest
import timeout_decorator
import ansible.plugins.action.debug as module_0

class Test_Debug_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\x07\xdf1\xda\x14\xbeJ\x88\xfe\xcc>\x0c\x90\xfd\x1c\xef\x80'
            float_0 = 2068.3803
            bool_0 = False
            dict_0 = {bool_0: float_0, bytes_0: bytes_0, bool_0: bytes_0, bool_0: bytes_0}
            bool_1 = True
            int_0 = 1876
            action_module_0 = module_0.ActionModule(bytes_0, float_0, bool_0, dict_0, bool_1, int_0)
            var_0 = action_module_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
