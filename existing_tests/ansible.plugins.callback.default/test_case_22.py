import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            callback_module_0 = module_0.CallbackModule()
            bytes_0 = b'\x03\xa0\xf9\xea\x1d\x8e\x10\xb1y\x0ex\xf9\x9ay\xe9\xcd'
            callback_module_1 = module_0.CallbackModule()
            var_0 = callback_module_1.v2_runner_retry(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
