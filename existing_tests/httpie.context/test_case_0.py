import unittest
import timeout_decorator
import httpie.context as module_0

class Test_Context_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        environment_0 = module_0.Environment()

if __name__ == "__main__":
    unittest.main()
