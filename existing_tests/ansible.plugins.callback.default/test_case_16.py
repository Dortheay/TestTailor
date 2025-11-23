import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            callback_module_0 = module_0.CallbackModule()
            int_0 = -33
            set_0 = {int_0, int_0, int_0, int_0, int_0, int_0}
            callback_module_1 = module_0.CallbackModule()
            var_0 = callback_module_1.v2_playbook_on_notify(int_0, set_0)
            bytes_0 = b'\xb9\x1a\x8a\xe4\x0c\x18\r\xe7(\x0e\xcaU\x02'
            var_1 = callback_module_0.v2_playbook_on_include(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
