import unittest
import timeout_decorator
import ansible.plugins.callback.junit as module_0

class Test_Junit_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = "d;'.n,Sw-1_~#P1"
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_playbook_on_play_start(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
