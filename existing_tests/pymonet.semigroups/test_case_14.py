import unittest
import timeout_decorator
import pymonet.semigroups as module_0

class Test_Semigroups_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 720
            max_0 = module_0.Max(int_0)
            var_0 = max_0.concat(max_0)
            dict_0 = {}
            bytes_0 = b'\x89#O\xc2\xf8,\x91\x9e\x0fz\xb9\xa2\xc6'
            last_0 = module_0.Last(bytes_0)
            float_0 = 4040.004
            map_0 = module_0.Map(float_0)
            list_0 = [bytes_0, var_0, max_0, map_0]
            min_0 = module_0.Min(list_0)
            first_0 = module_0.First(max_0)
            var_1 = first_0.concat(min_0)
            all_0 = module_0.All(last_0)
            first_1 = module_0.First(dict_0)
            str_0 = 'ws"iNuv@:(\tI8T0)'
            semigroup_0 = module_0.Semigroup(str_0)
            list_1 = []
            last_1 = module_0.Last(list_1)
            one_0 = module_0.One(list_1)
            one_1 = module_0.One(all_0)
            var_2 = last_0.concat(first_1)
            first_2 = module_0.First(list_1)
            map_1 = module_0.Map(first_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
