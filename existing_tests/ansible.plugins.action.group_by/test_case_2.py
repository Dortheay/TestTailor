import unittest
import timeout_decorator
import ansible.plugins.action.group_by as module_0

class Test_Group_by_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '!\x0cR4z4]-h*'
            int_0 = 94
            set_0 = {str_0}
            bool_0 = False
            str_1 = '=#*#pB/84M:RT15|R&h'
            list_0 = [bool_0, str_0, str_1, str_1]
            float_0 = 1817.1916
            action_module_0 = module_0.ActionModule(set_0, bool_0, set_0, list_0, float_0, int_0)
            tuple_0 = ()
            str_2 = '^s@VbSVUJ+nu\tqcMY/ '
            set_1 = {str_2, str_0}
            str_3 = ''
            str_4 = '772'
            int_1 = -1674
            action_module_1 = module_0.ActionModule(set_1, str_3, str_3, set_1, str_4, int_1)
            var_0 = action_module_1.run(action_module_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
