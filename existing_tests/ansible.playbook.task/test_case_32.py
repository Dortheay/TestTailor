import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            task_0 = module_0.Task()
            var_0 = task_0.serialize()
            task_1 = module_0.Task(task_0)
            var_1 = task_0.get_vars()
            var_2 = task_1.copy()
            list_0 = [task_1, task_0, task_1, task_0]
            str_0 = "'>^(!w@\rO"
            var_3 = task_1.load(list_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
