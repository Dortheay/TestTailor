import unittest
import timeout_decorator
import py_backwards.files as module_0

class Test_Files_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'ifilter'
            str_1 = 'p{'
            iterable_0 = module_0.get_input_output_paths(str_0, str_1, str_0)
            str_2 = 'nogex)stent.py'
            str_3 = 'output.py'
            iterable_1 = module_0.get_input_output_paths(str_3, str_2, str_3)
            str_4 = '~_n7I:Bp\\EHmZnB3\t'
            str_5 = '[\x0c9+.M(Q^aV'
            iterable_2 = module_0.get_input_output_paths(str_5, str_3, str_3)
            iterable_3 = module_0.get_input_output_paths(str_4, str_4, str_4)
            var_0 = None
            iterable_4 = module_0.get_input_output_paths(str_2, str_3, var_0)
            var_1 = list(iterable_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
