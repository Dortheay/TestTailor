import unittest
import timeout_decorator
import ansible.plugins.action.pause as module_0

class Test_Pause_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            ansible_timeout_exceeded_0 = module_0.AnsibleTimeoutExceeded()
            list_0 = []
            int_0 = -2223
            bool_0 = True
            float_0 = 100.0
            action_module_0 = module_0.ActionModule(list_0, list_0, int_0, bool_0, ansible_timeout_exceeded_0, float_0)
            var_0 = action_module_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
