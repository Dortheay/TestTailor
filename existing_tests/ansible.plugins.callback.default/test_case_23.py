import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            bytes_0 = None
            dict_0 = {}
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_playbook_on_notify(bytes_0, dict_0)
            bool_0 = False
            var_1 = callback_module_0.v2_on_file_diff(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
