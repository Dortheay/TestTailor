import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = 95
            semigroup_0 = module_0.Semigroup(int_0)
            semigroup_1 = module_0.Semigroup(semigroup_0)
            list_0 = [semigroup_1]
            str_0 = '>-5B8:5j!.)G@i`la,#'
            semigroup_2 = module_0.Semigroup(str_0)
            var_0 = semigroup_2.fold(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
