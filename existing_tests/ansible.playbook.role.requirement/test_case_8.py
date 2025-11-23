import unittest
import timeout_decorator
import ansible.playbook.role.requirement as module_0

class Test_Requirement_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            int_0 = None
            set_0 = {int_0, int_0, int_0}
            role_requirement_0 = module_0.RoleRequirement()
            var_0 = role_requirement_0.role_yaml_parse(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
