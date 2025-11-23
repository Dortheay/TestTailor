import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bytes_0 = b'ay\xcc\xd1/(\x89%'
        str_0 = 'b[\x0bw\x0c\t2!\t<mi\x0c6/$g1|'
        validation_0 = module_0.Validation(bytes_0, str_0)
        var_0 = validation_0.__str__()

if __name__ == "__main__":
    unittest.main()
