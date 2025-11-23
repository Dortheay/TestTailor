import unittest
import timeout_decorator
import ansible.playbook.role.requirement as module_0

class Test_Requirement_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'http://git.example.com/repos/repo.git'
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.role_yaml_parse(str_0)

if __name__ == "__main__":
    unittest.main()
