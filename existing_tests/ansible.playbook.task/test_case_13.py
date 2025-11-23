import unittest
import timeout_decorator
import ansible.playbook.task as module_0

class Test_Task_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        task_0 = module_0.Task()
        str_0 = 'vars'
        str_1 = 'action'
        str_2 = 'key'
        str_3 = 'value'
        str_4 = {str_2: str_3}
        str_5 = 'command'
        var_0 = {str_0: str_4, str_3: str_2, str_1: str_5}
        var_1 = task_0.get_first_parent_include()
        var_2 = task_0.preprocess_data(var_0)

if __name__ == "__main__":
    unittest.main()
