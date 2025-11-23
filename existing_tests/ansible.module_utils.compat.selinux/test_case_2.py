import unittest
import timeout_decorator
import ansible.module_utils.compat.selinux as module_0

class Test_Selinux_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '\n48"XMsVts~Mf%Ghy@V'
            var_0 = module_0.lgetfilecon_raw(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
