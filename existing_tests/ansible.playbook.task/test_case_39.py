import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_40(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            task_0 = module_0.Task()
            str_0 = 'parent'
            str_1 = 'parent_type'
            str_2 = 'implicit'
            str_3 = 'resolved_action'
            str_4 = 'TaskInclude'
            str_5 = 'role_naCme'
            str_6 = 'exml_role'
            str_7 = {str_5: str_6}
            bool_0 = True
            str_8 = 'action_resolved'
            var_0 = {str_0: str_7, str_1: str_4, str_2: str_7, str_2: bool_0, str_3: str_8}
            var_1 = task_0.deserialize(var_0)
            var_2 = task_0.preprocess_data(task_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
