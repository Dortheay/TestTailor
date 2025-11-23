import unittest
import timeout_decorator
import ansible.playbook.role.requirement as module_0

class Test_Requirement_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        role_requirement_0 = module_0.RoleRequirement()

if __name__ == "__main__":
    unittest.main()
