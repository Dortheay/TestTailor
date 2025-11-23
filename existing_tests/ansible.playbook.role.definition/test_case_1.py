import unittest
import timeout_decorator
import ansible.playbook.role.definition as module_0

class Test_Definition_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = False
            role_definition_0 = module_0.RoleDefinition()
            var_0 = role_definition_0.preprocess_data(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
