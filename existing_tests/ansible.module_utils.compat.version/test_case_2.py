import unittest
import timeout_decorator
import ansible.module_utils.compat.version as module_0

class Test_Version_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'Could not find apt-mark binary, not marking package(s) as manually installed.'
            version_0 = module_0.Version()
            var_0 = version_0.__eq__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
