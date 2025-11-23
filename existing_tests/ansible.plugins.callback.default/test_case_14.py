import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            list_0 = []
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_runner_item_on_failed(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
