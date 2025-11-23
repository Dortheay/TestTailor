import unittest
import timeout_decorator
import py_backwards.utils.helpers as module_0

class Test_Helpers_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        callable_0 = None
        module_0.debug(callable_0)

if __name__ == "__main__":
    unittest.main()
