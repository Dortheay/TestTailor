import unittest
import timeout_decorator
import ansible.playbook.task as module_0

class Test_Task_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        int_0 = -378
        task_0 = module_0.Task(int_0)
        var_0 = task_0.get_name()

if __name__ == "__main__":
    unittest.main()
