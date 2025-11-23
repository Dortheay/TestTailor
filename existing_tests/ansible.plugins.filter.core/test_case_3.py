import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = 1762.9609
            set_0 = set()
            var_0 = module_0.regex_findall(float_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
