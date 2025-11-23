import unittest
import timeout_decorator
import ansible.plugins.filter.mathstuff as module_0

class Test_Mathstuff_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        float_0 = -1088.8216
        dict_0 = {float_0: float_0, float_0: float_0}
        str_0 = '~l;);u*gtwP"?n{'
        dict_1 = {str_0: dict_0, str_0: str_0, str_0: str_0, str_0: float_0}
        var_0 = module_0.difference(float_0, dict_0, dict_1)

if __name__ == "__main__":
    unittest.main()
