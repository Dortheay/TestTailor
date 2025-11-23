import unittest
import timeout_decorator
import ansible.utils.hashing as module_0

class Test_Hashing_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'test string'
        var_0 = module_0.md5s(str_0)

if __name__ == "__main__":
    unittest.main()
