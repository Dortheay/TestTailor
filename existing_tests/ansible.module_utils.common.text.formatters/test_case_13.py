import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        bytes_0 = b'\xa4!\xf6'
        var_0 = module_0.lenient_lowercase(bytes_0)
        float_0 = 494.7903
        list_0 = [bytes_0, var_0]
        var_1 = module_0.bytes_to_human(float_0, list_0)

if __name__ == "__main__":
    unittest.main()
