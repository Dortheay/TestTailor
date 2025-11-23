import unittest
import timeout_decorator
import py_backwards.utils.helpers as module_0

class Test_Helpers_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            callable_0 = None
            str_0 = module_0.get_source(callable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
