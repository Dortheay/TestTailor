import unittest
import timeout_decorator
import ansible.template.vars as module_0

class Test_Vars_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = -964
            bool_0 = False
            tuple_0 = (bool_0,)
            int_1 = 401
            ansible_j2_vars_0 = module_0.AnsibleJ2Vars(tuple_0, tuple_0, int_1)
            var_0 = ansible_j2_vars_0.add_locals(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
