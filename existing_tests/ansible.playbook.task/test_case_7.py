import unittest
import timeout_decorator
import ansible.playbook.task as module_0

class Test_Task_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        task_0 = module_0.Task()
        var_0 = task_0.serialize()
        task_1 = module_0.Task(task_0)
        var_1 = task_0.get_vars()
        var_2 = task_1.serialize()

if __name__ == "__main__":
    unittest.main()
