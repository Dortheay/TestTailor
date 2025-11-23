import unittest
import timeout_decorator
import ansible.plugins.callback.junit as module_0

class Test_Junit_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = '=BM\x0b&aM'
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_runner_on_ok(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
