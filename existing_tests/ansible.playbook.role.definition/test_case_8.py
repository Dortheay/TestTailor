import unittest
import timeout_decorator
import ansible.playbook.role.definition as module_0

class Test_Definition_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        role_definition_0 = module_0.RoleDefinition()
        var_0 = role_definition_0.get_role_params()

if __name__ == "__main__":
    unittest.main()
