import unittest
import timeout_decorator
import ansible.playbook.role_include as module_0

class Test_Role_include_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        dict_0 = {}
        include_role_0 = module_0.IncludeRole(dict_0)
        var_0 = include_role_0.get_name()

if __name__ == "__main__":
    unittest.main()
