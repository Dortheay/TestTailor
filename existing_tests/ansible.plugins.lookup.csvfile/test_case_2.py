import unittest
import timeout_decorator
import ansible.plugins.lookup.csvfile as module_0

class Test_Csvfile_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        float_0 = -1604.3
        set_0 = {float_0, float_0, float_0}
        c_s_v_reader_0 = module_0.CSVReader(set_0)
        c_s_v_recoder_0 = module_0.CSVRecoder(c_s_v_reader_0)
        var_0 = c_s_v_recoder_0.__iter__()

if __name__ == "__main__":
    unittest.main()
