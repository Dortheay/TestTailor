import unittest
import timeout_decorator
import ansible.plugins.callback.junit as module_0

class Test_Junit_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            callback_module_0 = module_0.CallbackModule()
            float_0 = 0.0001
            bytes_0 = b'\xa01\xc4o\x8d\xa3v\x96\xac&\xb6'
            var_0 = callback_module_0.v2_runner_on_failed(float_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
