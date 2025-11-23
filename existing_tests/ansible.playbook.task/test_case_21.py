import unittest
import timeout_decorator
import ansible.playbook.task as module_0
import ansible.errors as module_1

class Test_Task_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'C>#]axmmRXM]{dI+Q*'
            task_0 = module_0.Task()
            var_0 = task_0.post_validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
