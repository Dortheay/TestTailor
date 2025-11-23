import unittest
import timeout_decorator
import ansible.module_utils.compat.version as module_0

class Test_Version_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '1.0'
        strict_version_0 = module_0.StrictVersion(str_0)
        var_0 = str(strict_version_0)
        str_1 = '2.3.4'
        strict_version_1 = module_0.StrictVersion(str_1)
        var_1 = str(strict_version_1)
        str_2 = '1.2.3a4'
        strict_version_2 = module_0.StrictVersion(str_2)
        var_2 = str(strict_version_2)
        str_3 = '3.0b2'
        strict_version_3 = module_0.StrictVersion(str_3)
        var_3 = str(strict_version_3)

if __name__ == "__main__":
    unittest.main()
