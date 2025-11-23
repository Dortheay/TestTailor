import unittest
import timeout_decorator
import ansible.plugins.callback.default as module_0

class Test_Default_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = 1862
            list_0 = [int_0]
            tuple_0 = (list_0,)
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_playbook_on_play_start(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
