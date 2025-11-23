import unittest
import timeout_decorator
import ansible.playbook.role.definition as module_0

class Test_Definition_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            role_definition_0 = module_0.RoleDefinition()
            str_0 = 'role'
            str_1 = 'test_role'
            str_2 = {str_0: str_1}
            var_0 = role_definition_0.preprocess_data(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
