import unittest
import timeout_decorator
import ansible.playbook.task_include as module_0

class Test_Task_include_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        task_include_0 = module_0.TaskInclude()
        var_0 = task_include_0.get_vars()

if __name__ == "__main__":
    unittest.main()
