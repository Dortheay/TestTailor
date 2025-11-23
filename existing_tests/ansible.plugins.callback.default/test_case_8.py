import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            callback_module_0 = module_0.CallbackModule()
            callback_module_1 = module_0.CallbackModule()
            float_0 = -2692.167
            list_0 = []
            var_0 = callback_module_1.v2_playbook_on_task_start(float_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
