import unittest
import timeout_decorator
import ansible.playbook.role.requirement as module_0

class Test_Requirement_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            role_requirement_0 = module_0.RoleRequirement()
            str_0 = 'REQUIREMENTS:%s\n'
            var_0 = role_requirement_0.role_yaml_parse(str_0)
            str_1 = '@7f+yha[8$d'
            var_1 = role_requirement_0.role_yaml_parse(var_0)
            set_0 = set()
            var_2 = role_requirement_0.repo_url_to_role_name(set_0)
            var_3 = role_requirement_0.role_yaml_parse(str_1)
            list_0 = []
            var_4 = role_requirement_0.role_yaml_parse(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
