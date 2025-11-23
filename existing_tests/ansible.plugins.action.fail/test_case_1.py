import unittest
import timeout_decorator
import ansible.plugins.action.fail as module_0

class Test_Fail_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = "No requirements found in file '%s'"
            str_1 = 'collections'
            bool_0 = False
            int_0 = 404
            list_0 = [bool_0, int_0, bool_0, int_0]
            str_2 = 'e>$y&kbE@BaL`ly|q'
            float_0 = 2808.679
            action_module_0 = module_0.ActionModule(str_1, bool_0, int_0, list_0, str_2, float_0)
            var_0 = action_module_0.run(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
