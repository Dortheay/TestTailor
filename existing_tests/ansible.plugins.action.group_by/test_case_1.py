import unittest
import timeout_decorator
import ansible.plugins.action.group_by as module_0

class Test_Group_by_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = False
            int_0 = -3067
            set_0 = {bool_0}
            bytes_0 = b'\xc6\xdb%\xfa\x11\xc9\xd3\xf7\x0e\xb8R}(\xf1\xe5\x14P\xcd6('
            int_1 = -3457
            action_module_0 = module_0.ActionModule(bool_0, int_0, set_0, bytes_0, set_0, int_1)
            var_0 = action_module_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
