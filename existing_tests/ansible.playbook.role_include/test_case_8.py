import unittest
import timeout_decorator
import ansible.playbook.role_include as module_0

class Test_Role_include_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.get_include_params()

if __name__ == "__main__":
    unittest.main()
