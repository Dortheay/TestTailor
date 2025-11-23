import unittest
import timeout_decorator
import ansible.module_utils.compat.selinux as module_0

class Test_Selinux_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            tuple_0 = None
            var_0 = module_0.lgetfilecon_raw(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
