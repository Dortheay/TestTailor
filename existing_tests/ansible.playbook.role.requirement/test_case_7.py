import unittest
import timeout_decorator
import ansible.playbook.role.requirement as module_0

class Test_Requirement_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = True
            role_requirement_0 = module_0.RoleRequirement()
            var_0 = role_requirement_0.role_yaml_parse(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
