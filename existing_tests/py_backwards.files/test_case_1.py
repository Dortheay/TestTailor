import unittest
import timeout_decorator
import py_backwards.files as module_0

class Test_Files_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'not_python.txt'
            str_1 = 'output.py'
            var_0 = None
            iterable_0 = module_0.get_input_output_paths(str_0, str_1, var_0)
            var_1 = list(iterable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
