import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = 1032
            bool_0 = None
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_playbook_on_notify(int_0, bool_0)
            callback_module_1 = module_0.CallbackModule()
            callback_module_2 = module_0.CallbackModule()
            int_1 = None
            callback_module_3 = module_0.CallbackModule()
            var_1 = callback_module_3.v2_playbook_on_no_hosts_remaining()
            var_2 = callback_module_3.v2_playbook_on_start(int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
