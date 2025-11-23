import unittest
import timeout_decorator
import ansible.plugins.callback.junit as module_0

class Test_Junit_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_stats(callback_module_0)

if __name__ == "__main__":
    unittest.main()
