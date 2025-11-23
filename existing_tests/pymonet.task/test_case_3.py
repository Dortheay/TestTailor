import unittest
import timeout_decorator
import pymonet.task as module_0

class Test_Task_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'm#n!*|@'
        list_0 = []
        task_0 = module_0.Task(list_0)
        var_0 = task_0.bind(str_0)

if __name__ == "__main__":
    unittest.main()
