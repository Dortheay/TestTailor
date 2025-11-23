import unittest
import timeout_decorator
import ansible.module_utils.common.validation as module_0

class Test_Validation_56(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = "U>'`JtJ{=i\x0c!sU"
        var_0 = module_0.check_type_dict(str_0)
        dict_0 = {}
        str_1 = '~nn_RL'
        tuple_0 = ()
        float_0 = -269.6
        var_1 = module_0.check_required_one_of(tuple_0, float_0)
        var_2 = module_0.check_required_arguments(dict_0, str_1)

if __name__ == "__main__":
    unittest.main()
