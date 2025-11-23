import unittest
import timeout_decorator
import ansible.constants as module_0

class Test_Constants_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bytes_0 = b'=\xc6\x87tK-r\x00\xa7V\xffb\xcbC\x9aQ\xe3\x1d'
        tuple_0 = ()
        deprecated_sequence_constant_0 = module_0._DeprecatedSequenceConstant(bytes_0, tuple_0, bytes_0)

if __name__ == "__main__":
    unittest.main()
