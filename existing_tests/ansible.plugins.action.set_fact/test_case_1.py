import unittest
import timeout_decorator
import ansible.plugins.action.set_fact as module_0

class Test_Set_fact_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = 1000.0
            bytes_0 = b'7\x1cx\x98'
            tuple_0 = (bytes_0,)
            set_0 = {tuple_0, float_0, float_0, float_0}
            bool_0 = True
            str_0 = '^-3\\H(3x1R%LN'
            action_module_0 = module_0.ActionModule(float_0, tuple_0, set_0, bool_0, str_0, set_0)
            var_0 = action_module_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
