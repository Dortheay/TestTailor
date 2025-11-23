import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            bool_0 = False
            dict_0 = {bool_0: bool_0}
            list_0 = [bool_0, dict_0, dict_0, bool_0]
            int_0 = 32768
            int_1 = -486
            bytes_0 = b'\xca\xf0.'
            int_2 = -1391
            dict_1 = {int_0: int_1, bytes_0: int_2}
            list_1 = module_0.reverse_map(dict_1)
            list_2 = [list_0, list_0]
            var_0 = module_0.map_structure_zip(dict_0, list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
