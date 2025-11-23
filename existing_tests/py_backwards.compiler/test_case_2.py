import unittest
import timeout_decorator
import py_backwards.compiler as module_0

class Test_Compiler_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = -126
            str_0 = 'input'
            int_1 = None
            tuple_0 = (int_0, int_1)
            compilation_result_0 = module_0.compile_files(str_0, str_0, tuple_0)
            str_1 = ''
            compilation_result_1 = module_0.compile_files(str_1, str_1, tuple_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
