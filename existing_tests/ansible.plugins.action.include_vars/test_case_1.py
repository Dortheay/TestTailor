import unittest
import timeout_decorator
import ansible.plugins.action.include_vars as module_0

class Test_Include_vars_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = 1428.7225
            int_0 = 32700
            int_1 = 1084
            set_0 = set()
            bytes_0 = b'\x90\xae:\xc4\xc4ku\xc1\xd2:QS'
            int_2 = -380
            str_0 = '*]vDt!hTg\x0c&j\\B'
            action_module_0 = module_0.ActionModule(int_0, int_1, set_0, bytes_0, int_2, str_0)
            var_0 = action_module_0.run(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
