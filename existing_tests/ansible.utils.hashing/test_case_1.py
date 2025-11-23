import unittest
import timeout_decorator
import ansible.utils.hashing as module_0

class Test_Hashing_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = 32700
        var_0 = module_0.secure_hash_s(int_0)

if __name__ == "__main__":
    unittest.main()
