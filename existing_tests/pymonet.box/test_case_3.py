import unittest
import timeout_decorator
import builtins as module_0
import pymonet.box as module_1

class Test_Box_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bool_0 = True
            bytes_0 = b'\x82\x04\x1d\xe9'
            box_0 = module_1.Box(bytes_0)
            object_0 = module_0.object()
            bytes_1 = b'u\xe8\xc1:\xb2\x1e\xb6\x83\xa9e\x01x\xf4\xb8\x17ZL\x99T'
            box_1 = module_1.Box(bytes_1)
            bool_1 = box_1.__eq__(object_0)
            var_0 = box_0.ap(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
