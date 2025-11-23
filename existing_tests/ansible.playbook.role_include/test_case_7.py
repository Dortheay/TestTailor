import unittest
import timeout_decorator
import ansible.playbook.role_include as module_0

class Test_Role_include_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = None
        include_role_0 = module_0.IncludeRole()
        var_0 = include_role_0.copy(str_0)

if __name__ == "__main__":
    unittest.main()
