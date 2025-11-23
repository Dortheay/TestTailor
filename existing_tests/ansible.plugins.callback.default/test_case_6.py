import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            callback_module_0 = None
            callback_module_1 = module_0.CallbackModule()
            var_0 = callback_module_1.v2_runner_on_unreachable(callback_module_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
