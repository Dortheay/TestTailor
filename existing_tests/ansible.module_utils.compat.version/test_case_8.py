import unittest
import timeout_decorator
import ansible.module_utils.compat.version as module_0

class Test_Version_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            version_0 = module_0.Version()
            str_0 = '6.}0Kz9ZP6|nQ4C]*H'
            loose_version_0 = module_0.LooseVersion(str_0)
            bool_0 = True
            var_0 = version_0.__le__(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
