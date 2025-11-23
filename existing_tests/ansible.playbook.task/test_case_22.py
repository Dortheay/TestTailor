import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '^4Hhg]ZIfoWL#=%*U'
            dict_0 = {str_0: str_0, str_0: str_0}
            task_0 = module_0.Task(dict_0, str_0)
            dict_1 = {str_0: str_0, str_0: str_0}
            tuple_0 = (dict_1,)
            dict_2 = {str_0: str_0}
            task_1 = module_0.Task(tuple_0, dict_2)
            var_0 = task_1.post_validate(task_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
