import unittest
import timeout_decorator
import py_backwards.compiler as module_0

class Test_Compiler_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '.'
            int_0 = None
            tuple_0 = (int_0, int_0)
            compilation_result_0 = module_0.compile_files(str_0, str_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
