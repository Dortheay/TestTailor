import unittest
import timeout_decorator
import ansible.executor.interpreter_discovery as module_0

class Test_Interpreter_discovery_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            interpreter_discovery_required_error_0 = None
            str_0 = 'w-\x0cA7tU}4I-Y\tEu'
            str_1 = '\t~F:uL '
            tuple_0 = (interpreter_discovery_required_error_0, str_0, str_1)
            int_0 = 2470
            interpreter_discovery_required_error_1 = module_0.InterpreterDiscoveryRequiredError(tuple_0, int_0, tuple_0)
            var_0 = interpreter_discovery_required_error_1.__repr__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
