import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            object_0 = module_1.object()
            bytes_0 = b'\xd6a\x0eWu\xe7\x02\xe7\xfd=\xb3\xbak\x94\xf3'
            right_0 = module_0.Right(bytes_0)
            right_1 = module_0.Right(right_0)
            var_0 = right_1.map(object_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
