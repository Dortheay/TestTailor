import unittest
import timeout_decorator
import ansible.modules.rpm_key as module_0

class Test_Rpm_key_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = 5760.05
        var_0 = module_0.is_pubkey(float_0)

if __name__ == "__main__":
    unittest.main()
