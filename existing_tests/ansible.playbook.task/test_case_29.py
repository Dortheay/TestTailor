import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            int_0 = -4776
            float_0 = 1719.01909
            task_0 = module_0.Task(int_0, float_0)
            task_1 = module_0.Task(task_0)
            var_0 = task_1.get_first_parent_include()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
