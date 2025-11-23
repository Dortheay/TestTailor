import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_63(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        str_0 = 'W,YT^&CAvZAN@/'
        float_0 = 0.5
        var_0 = module_0.to_bool(float_0)
        var_1 = module_0.regex_replace()
        dict_0 = {str_0: str_0, str_0: str_0}
        var_2 = module_0.randomize_list(dict_0, dict_0)

if __name__ == "__main__":
    unittest.main()
