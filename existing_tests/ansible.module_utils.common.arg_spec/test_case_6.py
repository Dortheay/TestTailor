import unittest
import timeout_decorator
import ansible.module_utils.common.arg_spec as module_0

class Test_Arg_spec_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        tuple_0 = ()
        dict_0 = {tuple_0: tuple_0}
        dict_1 = {tuple_0: dict_0}
        list_0 = [tuple_0, dict_0, tuple_0, dict_0]
        argument_spec_validator_0 = module_0.ArgumentSpecValidator(dict_1, list_0)

if __name__ == "__main__":
    unittest.main()
