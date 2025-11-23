import unittest
import timeout_decorator
import ansible.module_utils.compat.selinux as module_0

class Test_Selinux_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            var_0 = module_0.selinux_getenforcemode()
            float_0 = 536.93389
            dict_0 = {float_0: float_0, float_0: var_0}
            list_0 = [var_0, float_0, var_0]
            tuple_0 = (dict_0, list_0)
            tuple_1 = None
            var_1 = module_0.matchpathcon(tuple_0, tuple_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
