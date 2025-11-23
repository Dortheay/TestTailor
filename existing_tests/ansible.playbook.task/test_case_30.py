import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            task_0 = module_0.Task()
            var_0 = task_0.serialize()
            var_1 = task_0.__repr__()
            str_0 = 'zER D3'
            task_1 = module_0.Task(task_0)
            var_2 = task_0.get_vars()
            var_3 = task_1.copy()
            list_0 = [task_1, task_0, var_3, task_1, task_1, var_1]
            task_2 = module_0.Task(list_0)
            dict_0 = {str_0: var_2, var_3: list_0, var_1: var_0}
            var_4 = task_0.preprocess_data(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
