import unittest
import timeout_decorator
import py_backwards.files as module_0

class Test_Files_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'k7h,'
        iterable_0 = module_0.get_input_output_paths(str_0, str_0, str_0)

if __name__ == "__main__":
    unittest.main()
