import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = "o>'`JtJ{=i\x0c!sU"
            str_1 = "'&s\x0br2a"
            tuple_0 = (str_1,)
            var_0 = module_0.check_type_str(tuple_0, str_0)
            var_1 = module_0.check_type_dict(str_0)
            var_2 = module_0.check_type_dict(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
