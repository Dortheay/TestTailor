import unittest
import timeout_decorator
import ansible.plugins.callback.oneline as module_0

class Test_Oneline_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            dict_0 = {}
            bool_0 = False
            callback_module_0 = module_0.CallbackModule(bool_0)
            var_0 = callback_module_0.v2_runner_on_unreachable(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
