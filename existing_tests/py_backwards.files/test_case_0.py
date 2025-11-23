import unittest
import timeout_decorator
import py_backwards.files as module_0

class Test_Files_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'nonexistent.py'
            str_1 = 'output'
            iterable_0 = module_0.get_input_output_paths(str_0, str_1, str_0)
            var_0 = list(iterable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
