import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = 100.0
            tuple_0 = ()
            var_0 = module_0.strftime(float_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
