import unittest
import timeout_decorator
import ansible.plugins.action.pause as module_0

class Test_Pause_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            complex_0 = None
            int_0 = None
            var_0 = module_0.timeout_handler(complex_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
