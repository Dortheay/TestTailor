import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_28(self):
        try:
            float_0 = -1619.88
            var_0 = module_0.comment(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
