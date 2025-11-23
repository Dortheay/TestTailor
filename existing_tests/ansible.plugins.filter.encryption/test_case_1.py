import unittest
import timeout_decorator
import ansible.plugins.filter.encryption as module_0

class Test_Encryption_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '-di'
        bytes_0 = b'\x0f\xecI\xc8\xd1\x93\x8fm'
        var_0 = module_0.do_unvault(str_0, bytes_0)

if __name__ == "__main__":
    unittest.main()
