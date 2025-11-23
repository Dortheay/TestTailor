import unittest
import timeout_decorator
import pypara.commons.errors as module_0

class Test_Errors_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        programming_error_0 = module_0.ProgrammingError()

if __name__ == "__main__":
    unittest.main()
