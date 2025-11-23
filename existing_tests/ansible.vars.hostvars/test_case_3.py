import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            int_0 = -874
            host_vars_0 = module_0.HostVars(bool_0, bool_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
