import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b'~o\r\x1d\xf5\xcf\xf3\xf6'
        all_0 = module_0.All(bytes_0)
        list_0 = [bytes_0]
        min_0 = module_0.Min(list_0)
        var_0 = min_0.concat(min_0)
        str_0 = ')PeN]EBH_dCD'
        semigroup_0 = module_0.Semigroup(str_0)
        bytes_1 = b'8@U\xdcN\x98\r\xdb\xf8\x8550\xf2,\xb7'
        map_0 = module_0.Map(bytes_1)
        all_1 = all_0.concat(all_0)
        str_1 = all_1.__str__()
        max_0 = module_0.Max(semigroup_0)
        str_2 = max_0.__str__()

if __name__ == "__main__":
    unittest.main()
