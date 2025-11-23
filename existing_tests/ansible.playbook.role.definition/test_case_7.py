import unittest
import timeout_decorator
import ansible.playbook.role.definition as module_0

class Test_Definition_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        role_definition_0 = module_0.RoleDefinition()

if __name__ == "__main__":
    unittest.main()
