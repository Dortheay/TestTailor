import unittest
import timeout_decorator
import ansible.plugins.action.pause as module_0

class Test_Pause_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            ansible_timeout_exceeded_0 = None
            bytes_0 = None
            var_0 = module_0.is_interactive(bytes_0)
            set_0 = {ansible_timeout_exceeded_0, ansible_timeout_exceeded_0}
            dict_0 = {}
            var_1 = module_0.is_interactive(ansible_timeout_exceeded_0)
            str_0 = 'bW+dh'
            bool_0 = True
            dict_1 = {}
            action_module_0 = module_0.ActionModule(str_0, bool_0, dict_1, dict_0, set_0, str_0)
            var_2 = action_module_0.run(bytes_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
