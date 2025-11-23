import unittest
import timeout_decorator
import ansible.module_utils.compat.version as module_0

class Test_Version_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = 3515.0
            version_0 = module_0.Version()
            version_1 = module_0.Version()
            var_0 = version_1.__lt__(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
