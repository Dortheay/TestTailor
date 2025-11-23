import unittest
import timeout_decorator
import ansible.playbook.task_include as module_0

class Test_Task_include_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        task_include_0 = module_0.TaskInclude()

if __name__ == "__main__":
    unittest.main()
