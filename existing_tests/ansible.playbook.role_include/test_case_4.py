import unittest
import timeout_decorator
import ansible.playbook.role_include as module_0

class Test_Role_include_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            include_role_0 = module_0.IncludeRole()
            var_0 = include_role_0.get_name()
            set_0 = None
            var_1 = include_role_0.copy()
            var_2 = include_role_0.get_include_params()
            var_3 = include_role_0.copy()
            tuple_0 = (set_0,)
            var_4 = include_role_0.get_name()
            var_5 = include_role_0.get_name()
            include_role_1 = module_0.IncludeRole(include_role_0, tuple_0)
            var_6 = include_role_0.get_name()
            bytes_0 = None
            var_7 = include_role_1.copy(bytes_0)
            var_8 = include_role_1.get_include_params()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
