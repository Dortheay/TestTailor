import unittest
import timeout_decorator
import ansible.playbook.role.requirement as module_0

class Test_Requirement_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        role_requirement_0 = module_0.RoleRequirement()
        str_0 = '\r*/,ZEa.:L1,'
        var_0 = role_requirement_0.role_yaml_parse(str_0)
        role_requirement_1 = module_0.RoleRequirement()
        set_0 = set()
        var_1 = role_requirement_0.repo_url_to_role_name(set_0)
        var_2 = role_requirement_0.repo_url_to_role_name(set_0)
        role_requirement_2 = module_0.RoleRequirement()

if __name__ == "__main__":
    unittest.main()
