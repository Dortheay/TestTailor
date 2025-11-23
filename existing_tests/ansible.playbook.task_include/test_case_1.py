import unittest
import timeout_decorator
import ansible.playbook.task_include as module_0

class Test_Task_include_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = 824.04
            task_include_0 = module_0.TaskInclude()
            var_0 = task_include_0.check_options(task_include_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
