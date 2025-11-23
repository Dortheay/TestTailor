import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_38(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            task_0 = module_0.Task()
            str_0 = 'ansible.builtin'
            str_1 = 'vars'
            str_2 = 'action'
            str_3 = 'key'
            var_0 = task_0.__repr__()
            str_4 = {str_3: str_3}
            var_1 = []
            var_2 = {str_1: str_4, str_3: var_1, str_2: str_0}
            var_3 = task_0.preprocess_data(var_2)
            str_5 = 'Xh4(Gb<e'
            var_4 = task_0.preprocess_data(str_5)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
