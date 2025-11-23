import unittest
import timeout_decorator
import ansible.playbook.role.requirement as module_0

class Test_Requirement_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            role_requirement_0 = module_0.RoleRequirement()
            str_0 = 'Q%n$\x0cb\r.'
            role_requirement_1 = module_0.RoleRequirement()
            role_requirement_2 = module_0.RoleRequirement()
            var_0 = role_requirement_2.scm_archive_role(role_requirement_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
