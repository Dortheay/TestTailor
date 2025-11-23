import unittest
import timeout_decorator
import thonny.jedi_utils as module_0

class Test_Jedi_utils_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = True
            list_0 = [bool_0, bool_0]
            tuple_0 = (list_0,)
            var_0 = module_0.get_statement_of_position(bool_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
