import unittest
import timeout_decorator
import httpie.context as module_0

class Test_Context_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        environment_0 = module_0.Environment()
        var_0 = environment_0.__repr__()
        var_1 = environment_0.__str__()

if __name__ == "__main__":
    unittest.main()
