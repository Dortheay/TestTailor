import unittest
import timeout_decorator
import flutils.decorators as module_0

class Test_Decorators_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        pass

if __name__ == "__main__":
    unittest.main()
