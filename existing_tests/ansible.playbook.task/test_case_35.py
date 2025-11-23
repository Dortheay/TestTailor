import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_36(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            str_0 = 'parent'
            str_1 = 'parent_type'
            str_2 = 'role'
            str_3 = 'implicit'
            str_4 = 'resolved_actio1n'
            str_5 = 'some_parent_key'
            str_6 = 'some_parent_value'
            str_7 = {str_5: str_6}
            str_8 = 'some_role_key'
            str_9 = 'some_role_value'
            str_10 = {str_8: str_9}
            bool_0 = True
            str_11 = 'some_action'
            var_0 = {str_0: str_7, str_1: str_7, str_2: str_10, str_3: bool_0, str_4: str_11}
            task_0 = module_0.Task()
            var_1 = task_0.deserialize(var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
