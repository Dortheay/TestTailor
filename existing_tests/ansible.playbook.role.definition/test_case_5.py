import unittest
import timeout_decorator
import ansible.playbook.role.definition as module_0

class Test_Definition_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bytes_0 = b'\xd42\x11\x9d\xdd\xb8\x1f'
            str_0 = "Xpt<z;S}j$pJ'$|*\x0c)"
            dict_0 = {bytes_0: str_0}
            bool_0 = False
            role_definition_0 = module_0.RoleDefinition(dict_0, bool_0)
            var_0 = role_definition_0.get_role_path()
            float_0 = -3015.70099
            set_0 = {str_0, bytes_0}
            role_definition_1 = module_0.RoleDefinition(set_0)
            role_definition_2 = module_0.RoleDefinition(bytes_0, set_0, role_definition_1)
            role_definition_3 = module_0.RoleDefinition(bytes_0, float_0, role_definition_2)
            var_1 = role_definition_3.get_name(str_0)
            str_1 = 'bphN2'
            int_0 = 148
            bytes_1 = b'?\x99\xfad\xa6\x16t\x88(V\x00\xaa\xe0\xe8'
            float_1 = 0.001
            role_definition_4 = module_0.RoleDefinition(int_0, bytes_1, float_1, bytes_1)
            var_2 = role_definition_4.preprocess_data(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
