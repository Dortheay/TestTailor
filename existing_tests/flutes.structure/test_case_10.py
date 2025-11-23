import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bool_0 = False
            set_0 = {bool_0, bool_0}
            tuple_0 = (set_0,)
            bytes_0 = b'\xdcbQ\\'
            tuple_1 = (tuple_0, bytes_0)
            var_0 = module_0.map_structure(bool_0, tuple_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
