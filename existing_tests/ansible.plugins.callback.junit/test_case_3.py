import unittest
import timeout_decorator
import ansible.plugins.callback.junit as module_0

class Test_Junit_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_runner_on_no_hosts(callback_module_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
