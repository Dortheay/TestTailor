import unittest
import timeout_decorator
import ansible.playbook.task as module_0

class Test_Task_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        task_0 = module_0.Task()
        var_0 = task_0.serialize()
        var_1 = task_0.__repr__()
        var_2 = task_0.get_include_params()
        task_1 = module_0.Task(task_0)
        var_3 = task_0.get_vars()
        var_4 = task_1.get_include_params()
        var_5 = task_1.copy()

if __name__ == "__main__":
    unittest.main()
