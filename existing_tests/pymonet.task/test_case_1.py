import unittest
import timeout_decorator
import pymonet.task as module_0

class Test_Task_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = "%\tYkJ',&*+JN_!e}?"
        task_0 = module_0.Task(str_0)

if __name__ == "__main__":
    unittest.main()
