import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            task_0 = module_0.Task()
            var_0 = task_0.serialize()
            str_0 = 'zER D3'
            task_1 = module_0.Task(task_0)
            var_1 = task_0.get_vars()
            var_2 = task_1.copy()
            float_0 = 1000.0
            var_3 = task_1.copy(float_0)
            list_0 = [task_1, task_0, task_1, task_0]
            var_4 = task_1.serialize()
            var_5 = task_1.load(list_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
