import unittest
import timeout_decorator
import ansible.playbook.task_include as module_0

class Test_Task_include_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            list_0 = []
            task_include_0 = module_0.TaskInclude()
            var_0 = task_include_0.copy()
            str_0 = None
            task_include_1 = module_0.TaskInclude(list_0, str_0)
            float_0 = 824.04
            task_include_2 = module_0.TaskInclude()
            var_1 = task_include_2.check_options(task_include_1, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
