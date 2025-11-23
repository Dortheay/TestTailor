import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            int_0 = -33
            set_0 = {int_0, int_0}
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_playbook_on_notify(int_0, set_0)
            var_1 = callback_module_0.v2_runner_item_on_skipped(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
