import unittest
import timeout_decorator
import ansible.playbook.role.definition as module_0

class Test_Definition_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            float_0 = -886.4
            role_definition_0 = module_0.RoleDefinition(float_0)
            var_0 = role_definition_0.get_role_path()
            dict_0 = {}
            var_1 = role_definition_0.preprocess_data(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
