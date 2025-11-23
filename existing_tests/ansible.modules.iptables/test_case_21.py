import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            bytes_0 = b'\t-'
            bytes_1 = b"\xe7\xa6\xde\xd5'\xf6Z\xd0\x08\x93"
            float_0 = 531.33
            var_0 = module_0.insert_rule(bytes_0, bytes_1, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
