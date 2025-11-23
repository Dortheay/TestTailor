import unittest
import timeout_decorator
import ansible.playbook.role.requirement as module_0

class Test_Requirement_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        role_requirement_0 = module_0.RoleRequirement()
        str_0 = 'DFV3U#(O-I`SIc'
        var_0 = role_requirement_0.role_yaml_parse(str_0)
        str_1 = "@aWL]E'\\\r6)L"
        var_1 = role_requirement_0.role_yaml_parse(str_1)

if __name__ == "__main__":
    unittest.main()
