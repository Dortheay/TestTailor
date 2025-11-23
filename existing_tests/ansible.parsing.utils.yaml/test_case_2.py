import unittest
import timeout_decorator
import ansible.parsing.utils.yaml as module_0

class Test_Yaml_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = ']U|GaKg'
            str_1 = "24~|'(t8'\t]cvLlV"
            float_0 = None
            var_0 = module_0.from_yaml(str_0, str_1, float_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
