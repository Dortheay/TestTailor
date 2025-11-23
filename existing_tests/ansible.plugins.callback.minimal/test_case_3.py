import unittest
import timeout_decorator
import ansible.plugins.callback.minimal as module_0

class Test_Minimal_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            callback_module_0 = module_0.CallbackModule()
            dict_0 = {callback_module_0: callback_module_0, callback_module_0: callback_module_0, callback_module_0: callback_module_0}
            var_0 = callback_module_0.v2_runner_on_skipped(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
