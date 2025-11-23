import unittest
import timeout_decorator
import ansible.playbook.task as module_0

class Test_Task_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        task_0 = module_0.Task()
        str_0 = ''
        str_1 = [str_0]
        str_2 = 'action'
        str_3 = 'key'
        str_4 = 'value'
        str_5 = 'command'
        var_0 = {str_3: str_1, str_4: str_3, str_2: str_5}
        var_1 = task_0.preprocess_data(var_0)

if __name__ == "__main__":
    unittest.main()
