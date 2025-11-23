import unittest
import timeout_decorator
import ansible.playbook.role_include as module_0

class Test_Role_include_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            include_role_0 = module_0.IncludeRole()
            str_0 = 'Invalid conditional detected: %s'
            var_0 = include_role_0.load(include_role_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
