import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            task_0 = module_0.Task()
            var_0 = task_0.serialize()
            var_1 = task_0.__repr__()
            var_2 = task_0.get_include_params()
            task_1 = module_0.Task(task_0)
            var_3 = task_0.get_vars()
            var_4 = task_1.get_include_params()
            var_5 = task_1.copy()
            str_0 = "'>^(!w@\rO"
            var_6 = task_1.get_vars()
            dict_0 = None
            var_7 = task_0.get_first_parent_include()
            task_2 = module_0.Task(dict_0)
            var_8 = task_0.load(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
