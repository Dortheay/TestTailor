import unittest
import timeout_decorator
import ansible.playbook.role.requirement as module_0

class Test_Requirement_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            tuple_0 = ()
            role_requirement_0 = module_0.RoleRequirement()
            dict_0 = {tuple_0: role_requirement_0, tuple_0: role_requirement_0}
            role_requirement_1 = module_0.RoleRequirement()
            var_0 = role_requirement_1.role_yaml_parse(dict_0)
            bool_0 = True
            role_requirement_2 = module_0.RoleRequirement()
            var_1 = role_requirement_2.role_yaml_parse(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
