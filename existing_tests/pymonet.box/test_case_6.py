import unittest
import timeout_decorator
import pymonet.box as module_0
import builtins as module_1

class Test_Box_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b'\x82\x04\x1d\xe9'
        box_0 = module_0.Box(bytes_0)
        object_0 = module_1.object()
        bool_0 = box_0.__eq__(object_0)

if __name__ == "__main__":
    unittest.main()
