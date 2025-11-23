import unittest
import timeout_decorator
import ansible.executor.interpreter_discovery as module_0

class Test_Interpreter_discovery_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        float_0 = -3105.52
        dict_0 = {}
        interpreter_discovery_required_error_0 = module_0.InterpreterDiscoveryRequiredError(float_0, float_0, dict_0)

if __name__ == "__main__":
    unittest.main()
