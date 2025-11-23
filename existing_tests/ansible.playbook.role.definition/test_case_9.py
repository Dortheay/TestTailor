import unittest
import timeout_decorator
import ansible.playbook.role.definition as module_0

class Test_Definition_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b'\xb0\x94'
        role_definition_0 = module_0.RoleDefinition(bytes_0)
        var_0 = role_definition_0.get_role_path()

if __name__ == "__main__":
    unittest.main()
