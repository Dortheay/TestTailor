import unittest
import timeout_decorator
import ansible.plugins.callback.junit as module_0

class Test_Junit_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            callback_module_0 = module_0.CallbackModule()
            int_0 = 227
            str_0 = "PFx'~yRWD=xg^"
            list_0 = [str_0, int_0, str_0]
            callback_module_1 = module_0.CallbackModule()
            var_0 = callback_module_1.v2_playbook_on_task_start(str_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
