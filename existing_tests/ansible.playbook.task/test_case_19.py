import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            task_0 = module_0.Task()
            dict_0 = {}
            var_0 = task_0.preprocess_data(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
