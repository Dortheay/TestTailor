import unittest
import timeout_decorator
import ansible.plugins.lookup.csvfile as module_0

class Test_Csvfile_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = False
            int_0 = -2839
            str_0 = 'EOoH\x0b"_dMaq1t0hk"'
            c_s_v_recoder_0 = module_0.CSVRecoder(str_0)
            c_s_v_reader_0 = module_0.CSVReader(int_0)
            var_0 = c_s_v_reader_0.__iter__()
            set_0 = set()
            c_s_v_reader_1 = module_0.CSVReader(bool_0, set_0)
            lookup_module_0 = module_0.LookupModule()
            c_s_v_recoder_1 = module_0.CSVRecoder(c_s_v_reader_1, lookup_module_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
