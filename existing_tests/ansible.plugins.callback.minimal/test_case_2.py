import unittest
import timeout_decorator
import ansible.plugins.callback.minimal as module_0

class Test_Minimal_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\xef\xf8\xf9\xd2;'
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_runner_on_ok(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
