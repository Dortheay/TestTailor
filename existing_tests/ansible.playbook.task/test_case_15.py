import unittest
import timeout_decorator
import ansible.playbook.task as module_0

class Test_Task_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        task_0 = module_0.Task()
        str_0 = 'parent'
        str_1 = 'parent_type'
        str_2 = 'implicit'
        str_3 = 'resolved_action'
        str_4 = 'TaskInclude'
        str_5 = 'role_name'
        str_6 = 'example_role'
        str_7 = {str_5: str_6}
        bool_0 = True
        str_8 = 'action_resolved'
        var_0 = {str_0: str_7, str_1: str_4, str_2: str_7, str_2: bool_0, str_3: str_8}
        var_1 = task_0.deserialize(var_0)
        var_2 = task_0._parent
        var_3 = task_0._role

if __name__ == "__main__":
    unittest.main()
