import unittest
import timeout_decorator
import ansible.playbook.role.definition as module_0

class Test_Definition_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        float_0 = -1555.81604
        int_0 = 600
        role_definition_0 = module_0.RoleDefinition(int_0, float_0)
        var_0 = role_definition_0.get_name(float_0)

if __name__ == "__main__":
    unittest.main()
