import unittest
import timeout_decorator
import ansible.playbook.task as module_0

class Test_Task_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        task_0 = module_0.Task()
        var_0 = task_0.get_vars()

if __name__ == "__main__":
    unittest.main()
