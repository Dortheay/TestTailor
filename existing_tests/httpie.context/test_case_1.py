import unittest
import timeout_decorator
import httpie.context as module_0

class Test_Context_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        environment_0 = module_0.Environment()
        var_0 = environment_0.__repr__()

if __name__ == "__main__":
    unittest.main()
