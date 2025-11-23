import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '%i,;6eE)s-'
            var_0 = module_0.camel_case_to_snake(str_0)
            str_1 = module_0.strip_html(str_0)
            str_2 = '%+x*Cp&;*}IHlIA3r&'
            str_3 = module_0.asciify(str_2)
            int_0 = -3518
            str_4 = module_0.compress(str_0, str_2, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
