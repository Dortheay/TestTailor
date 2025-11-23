import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bytes_0 = b'j\x93'
        var_0 = module_0.is_sequence(bytes_0)

if __name__ == "__main__":
    unittest.main()
