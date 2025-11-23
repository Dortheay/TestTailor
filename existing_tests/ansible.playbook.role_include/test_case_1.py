import unittest
import timeout_decorator
import ansible.playbook.role_include as module_0

class Test_Role_include_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = 588.47
            bool_0 = False
            include_role_0 = module_0.IncludeRole(bool_0)
            var_0 = include_role_0.get_block_list(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
