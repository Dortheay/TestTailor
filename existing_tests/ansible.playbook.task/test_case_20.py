import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            tuple_0 = None
            task_0 = module_0.Task()
            var_0 = task_0.preprocess_data(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
