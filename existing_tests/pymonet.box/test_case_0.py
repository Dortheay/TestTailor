import unittest
import timeout_decorator
import builtins as module_0
import pymonet.box as module_1

class Test_Box_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = {}
            object_0 = module_0.object(**dict_0)
            float_0 = 2592.0
            box_0 = module_1.Box(float_0)
            bool_0 = box_0.__eq__(object_0)
            bytes_0 = b'\x85\xbd\xab\xefIZ>\xfe'
            box_1 = module_1.Box(bytes_0)
            var_0 = box_1.to_maybe()
            var_1 = box_1.to_lazy()
            var_2 = box_1.to_either()
            str_0 = box_1.__str__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
