import unittest
import timeout_decorator
import py_backwards.types as module_0

class Test_Types_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            compilation_result_0 = module_0.CompilationResult()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
