import unittest
import timeout_decorator
import py_backwards.compiler as module_0

class Test_Compiler_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'cStringIO'
        int_0 = -1001
        tuple_0 = (int_0, int_0)
        compilation_result_0 = module_0.compile_files(str_0, str_0, tuple_0)

if __name__ == "__main__":
    unittest.main()
