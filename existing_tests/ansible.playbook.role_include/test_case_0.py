import unittest
import timeout_decorator
import ansible.playbook.role_include as module_0

class Test_Role_include_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = None
            float_1 = 2919.52
            include_role_0 = module_0.IncludeRole()
            var_0 = include_role_0.get_block_list(float_0, float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
