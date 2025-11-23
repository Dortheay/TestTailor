import unittest
import timeout_decorator
import ansible.plugins.action.fetch as module_0

class Test_Fetch_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '"8W\r8lK\\'
            bool_0 = False
            set_0 = {bool_0, str_0, str_0}
            str_1 = 'tv '
            float_0 = 4219.7
            action_module_0 = module_0.ActionModule(str_0, bool_0, set_0, set_0, str_1, float_0)
            var_0 = action_module_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
