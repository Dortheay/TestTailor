import unittest
import timeout_decorator
import ansible.plugins.callback.minimal as module_0

class Test_Minimal_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            callback_module_0 = module_0.CallbackModule()
            dict_0 = {}
            var_0 = callback_module_0.v2_on_file_diff(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
