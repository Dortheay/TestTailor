import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        callback_module_0 = module_0.CallbackModule()
        str_0 = 'qP'
        var_0 = callback_module_0.v2_playbook_on_notify(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
