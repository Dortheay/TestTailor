import unittest
import timeout_decorator
import ansible.plugins.callback.oneline as module_0

class Test_Oneline_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = True
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_runner_on_ok(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
