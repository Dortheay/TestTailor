import unittest
import timeout_decorator
import ansible.plugins.action.unarchive as module_0

class Test_Unarchive_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\xf4\xb7s\xda\xc5\x1c\x84\x1a\xba\x8c\xa5^\xe1\xb05\xb0^]\xb8'
            set_0 = {bytes_0}
            str_0 = 'u31oW2Aho4nyIw}BC)\r'
            float_0 = 0.1
            tuple_0 = ()
            action_module_0 = module_0.ActionModule(set_0, str_0, set_0, bytes_0, float_0, tuple_0)
            int_0 = -553
            str_1 = 'KT-(*E6Jr?No1!7.d'
            action_module_1 = module_0.ActionModule(bytes_0, set_0, str_0, action_module_0, int_0, str_1)
            var_0 = action_module_1.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
