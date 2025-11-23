import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'j31EHpgS'
            bool_0 = False
            task_0 = module_0.Task(bool_0)
            var_0 = task_0.get_name()
            task_1 = module_0.Task()
            task_2 = module_0.Task(str_0, task_1)
            var_1 = task_1.get_first_parent_include()
            bool_1 = True
            float_0 = -472.00819
            task_3 = module_0.Task(bool_1, float_0)
            task_4 = module_0.Task()
            int_0 = 650
            set_0 = {task_2, int_0}
            var_2 = task_2.preprocess_data(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
