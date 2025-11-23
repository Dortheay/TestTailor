import unittest
import timeout_decorator
import ansible.utils.hashing as module_0

class Test_Hashing_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        set_0 = None
        var_0 = module_0.secure_hash(set_0)

if __name__ == "__main__":
    unittest.main()
