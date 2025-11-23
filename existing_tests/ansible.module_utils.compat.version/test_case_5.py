import unittest
import timeout_decorator
import ansible.module_utils.compat.version as module_0

class Test_Version_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '6F%J'
            version_0 = module_0.Version()
            var_0 = version_0.__ge__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
