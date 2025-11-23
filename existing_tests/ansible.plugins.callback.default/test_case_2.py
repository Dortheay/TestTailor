import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.set_options()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
