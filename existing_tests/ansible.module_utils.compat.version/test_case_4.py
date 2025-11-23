import unittest
import timeout_decorator
import ansible.module_utils.compat.version as module_0

class Test_Version_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bool_0 = False
            version_0 = module_0.Version()
            var_0 = version_0.__gt__(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
