import unittest
import timeout_decorator
import ansible.playbook.task as module_0

class Test_Task_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        task_0 = module_0.Task()
        var_0 = task_0.serialize()
        var_1 = task_0.copy()

if __name__ == "__main__":
    unittest.main()
