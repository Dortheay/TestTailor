import unittest
import timeout_decorator
import pymonet.box as module_0
import builtins as module_1

class Test_Box_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        bytes_0 = b'\x8a\x18C\x98\xd2\xae\x18\x07/'
        box_0 = module_0.Box(bytes_0)
        var_0 = box_0.to_validation()

if __name__ == "__main__":
    unittest.main()
