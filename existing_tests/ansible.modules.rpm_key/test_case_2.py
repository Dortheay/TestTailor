import unittest
import timeout_decorator
import ansible.modules.rpm_key as module_0

class Test_Rpm_key_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = -376.0
            rpm_key_0 = module_0.RpmKey(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
