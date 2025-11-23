import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'Qagh}'
            dict_0 = {str_0: str_0, str_0: str_0}
            bool_0 = False
            tuple_0 = (dict_0, bool_0)
            var_0 = module_0.map_structure_zip(str_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
