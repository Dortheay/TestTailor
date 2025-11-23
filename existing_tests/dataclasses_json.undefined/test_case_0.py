import unittest
import timeout_decorator
import dataclasses_json.undefined as module_0

class Test_Undefined_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            undefined_parameter_action_0 = module_0._UndefinedParameterAction()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
