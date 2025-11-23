import unittest
import timeout_decorator
import ansible.playbook.role.requirement as module_0

class Test_Requirement_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 's0ippey, since %s does not exGst'
        role_requirement_0 = module_0.RoleRequirement()
        var_0 = role_requirement_0.role_yaml_parse(str_0)

if __name__ == "__main__":
    unittest.main()
