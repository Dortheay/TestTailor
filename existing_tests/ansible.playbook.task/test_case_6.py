import unittest
import timeout_decorator
import ansible.playbook.task as module_0

class Test_Task_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        task_0 = module_0.Task()
        var_0 = task_0.serialize()

if __name__ == "__main__":
    unittest.main()
