import unittest
import timeout_decorator
import httpie.context as module_0

class Test_Context_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        environment_0 = module_0.Environment()
        var_0 = environment_0.__repr__()
        environment_1 = module_0.Environment()
        var_1 = environment_0.__str__()
        var_2 = environment_1.log_error(environment_1)

if __name__ == "__main__":
    unittest.main()
