import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            bytes_0 = b'\x9d\xda\xd3\xf0\xd1*\xbd\x83\xb5\xf3\xd2'
            int_0 = 480
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_runner_on_start(bytes_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
