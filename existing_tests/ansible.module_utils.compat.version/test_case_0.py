import unittest
import timeout_decorator
import ansible.module_utils.compat.version as module_0

class Test_Version_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '`\x0b}[[-h'
            strict_version_0 = module_0.StrictVersion(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
