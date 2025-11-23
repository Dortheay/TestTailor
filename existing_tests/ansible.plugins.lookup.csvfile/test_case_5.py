import unittest
import timeout_decorator
import ansible.plugins.lookup.csvfile as module_0

class Test_Csvfile_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = False
            set_0 = {bool_0, bool_0, bool_0}
            c_s_v_reader_0 = module_0.CSVReader(set_0)
            var_0 = c_s_v_reader_0.__next__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
