import unittest
import timeout_decorator
import pymonet.either as module_0
import builtins as module_1

class Test_Either_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b'\xa7\xae\x00'
        either_0 = module_0.Either(bytes_0)
        object_0 = None
        bool_0 = either_0.__eq__(object_0)
        var_0 = either_0.to_lazy()

if __name__ == "__main__":
    unittest.main()
