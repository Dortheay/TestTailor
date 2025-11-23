import unittest
import timeout_decorator
import ansible.playbook.role.definition as module_0

class Test_Definition_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = None
            int_0 = -62
            role_definition_0 = module_0.RoleDefinition(int_0)
            var_0 = role_definition_0.load(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
