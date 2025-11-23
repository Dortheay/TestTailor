import unittest
import timeout_decorator
import ansible.playbook.task_include as module_0

class Test_Task_include_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        task_include_0 = module_0.TaskInclude()
        str_0 = 'action'
        str_1 = 'args'
        str_2 = 'loop'
        str_3 = 'some_valid_action'
        var_0 = {}
        str_4 = 'some_loop'
        var_1 = {str_0: str_3, str_1: var_0, str_2: str_4}
        str_5 = 'invalid_attr'
        var_2 = {}
        str_6 = 'not_a_valid_keyword'
        var_3 = {str_0: str_3, str_1: var_2, str_5: str_6}
        var_4 = task_include_0.preprocess_data(var_1)
        var_5 = task_include_0.preprocess_data(var_3)

if __name__ == "__main__":
    unittest.main()
