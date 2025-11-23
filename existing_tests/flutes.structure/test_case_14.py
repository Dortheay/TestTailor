import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            set_0 = None
            bytes_0 = b'\xe08\x0b'
            int_0 = 529
            var_0 = module_0.no_map_instance(bytes_0)
            var_1 = None
            int_1 = -1549
            dict_0 = {var_1: int_0, var_1: int_1, var_1: int_1, var_1: int_1}
            list_0 = module_0.reverse_map(dict_0)
            str_0 = '0Eu\rctqi&#'
            var_2 = module_0.map_structure_zip(set_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
