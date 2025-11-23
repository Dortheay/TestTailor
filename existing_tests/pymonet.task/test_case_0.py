import unittest
import timeout_decorator
import pymonet.task as module_0

class Test_Task_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
