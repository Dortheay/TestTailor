import unittest
import timeout_decorator
import ansible.playbook.role.definition as module_0

class Test_Definition_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            role_definition_0 = module_0.RoleDefinition()
            var_0 = role_definition_0.get_role_params()
            int_0 = -1944
            role_definition_1 = module_0.RoleDefinition(int_0)
            var_1 = role_definition_1.get_name()
            var_2 = role_definition_1.get_role_path()
            float_0 = -1040.727205
            role_definition_2 = module_0.RoleDefinition(float_0)
            var_3 = role_definition_1.get_role_path()
            complex_0 = None
            var_4 = role_definition_1.get_name(complex_0)
            var_5 = role_definition_1.get_role_path()
            list_0 = [var_4, complex_0]
            tuple_0 = (list_0,)
            str_0 = "<*nV'7N~gwVG"
            role_definition_3 = module_0.RoleDefinition(str_0)
            bool_0 = False
            role_definition_4 = module_0.RoleDefinition(bool_0)
            var_6 = role_definition_3.preprocess_data(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
