import unittest
import timeout_decorator
import ansible.plugins.lookup.csvfile as module_0

class Test_Csvfile_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            dict_0 = {}
            lookup_module_0 = module_0.LookupModule(**dict_0)
            int_0 = -2607
            c_s_v_reader_0 = module_0.CSVReader(int_0, dict_0)
            int_1 = 200000
            var_0 = lookup_module_0.run(int_1, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
