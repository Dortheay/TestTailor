import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = 0.5
            var_0 = module_0.human_to_bytes(float_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
