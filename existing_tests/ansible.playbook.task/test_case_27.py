import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = 'A{('
            int_0 = 162
            int_1 = -1449
            tuple_0 = (int_0, int_1)
            task_0 = module_0.Task(str_0, tuple_0)
            var_0 = task_0.all_parents_static()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
