import unittest
import timeout_decorator
import ansible.playbook.role_include as module_0

class Test_Role_include_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        include_role_0 = module_0.IncludeRole()

if __name__ == "__main__":
    unittest.main()
