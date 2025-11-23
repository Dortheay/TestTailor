import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            task_0 = module_0.Task()
            str_0 = 'vars'
            str_1 = 'collections'
            str_2 = 'ation'
            str_3 = 'key'
            str_4 = 'value'
            str_5 = {str_3: str_4}
            var_0 = []
            str_6 = 'command'
            var_1 = {str_0: str_5, str_1: var_0, str_2: str_6}
            var_2 = task_0.preprocess_data(var_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
