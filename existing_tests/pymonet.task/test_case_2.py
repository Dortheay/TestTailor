import unittest
import timeout_decorator
import pymonet.task as module_0

class Test_Task_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'k}..riV;'
        bool_0 = True
        task_0 = module_0.Task(bool_0)
        var_0 = task_0.map(str_0)

if __name__ == "__main__":
    unittest.main()
