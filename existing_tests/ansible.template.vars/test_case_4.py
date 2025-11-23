import unittest
import timeout_decorator
import ansible.template.vars as module_0

class Test_Vars_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'U~dc8?H|L759Hy'
            ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_0, str_0)
            var_0 = ansible_j2_vars_0.__contains__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
