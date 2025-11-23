import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            lookup_module_0 = module_0.LookupModule()
            str_0 = '5'
            str_1 = [str_0]
            var_0 = {}
            var_1 = lookup_module_0.run(str_1, var_0)
            str_2 = '5-8'
            str_3 = [str_2]
            var_2 = lookup_module_0.run(str_3, var_0)
            str_4 = '2-10/2'
            str_5 = [str_4]
            var_3 = lookup_module_0.run(str_5, var_0)
            str_6 = '4:host%02d'
            str_7 = [str_6]
            var_4 = lookup_module_0.run(str_7, var_0)
            str_8 = 'start=5 end=11 stride=2 format=0x%02x'
            str_9 = [str_8]
            var_5 = lookup_module_0.run(str_9, var_0)
            str_10 = 'count=5'
            str_11 = [str_10]
            var_6 = lookup_module_0.run(str_11, var_0)
            str_12 = '10-1/1:-%02d'
            str_13 = [str_12]
            var_7 = lookup_module_0.run(str_13, var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
