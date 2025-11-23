import unittest
import timeout_decorator
import ansible.utils.hashing as module_0

class Test_Hashing_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bytes_0 = b'p'
        var_0 = module_0.md5(bytes_0)

if __name__ == "__main__":
    unittest.main()
