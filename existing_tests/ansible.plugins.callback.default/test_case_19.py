import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            callback_module_0 = module_0.CallbackModule()
            str_0 = 'g>DU~[an%Y_O0}M?`/'
            var_0 = callback_module_0.v2_runner_on_async_poll(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
