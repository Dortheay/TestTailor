import unittest
import timeout_decorator
import ansible.playbook.task as module_0

class Test_Task_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        task_0 = module_0.Task()

if __name__ == "__main__":
    unittest.main()
