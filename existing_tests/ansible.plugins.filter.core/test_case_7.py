import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            set_0 = None
            bool_0 = False
            var_0 = module_0.rand(set_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
