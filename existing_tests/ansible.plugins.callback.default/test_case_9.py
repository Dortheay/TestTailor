import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            callback_module_0 = module_0.CallbackModule()
            str_0 = 'tG7ti3'
            var_0 = callback_module_0.v2_playbook_on_cleanup_task_start(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
