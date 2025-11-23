import unittest
import timeout_decorator
import ansible.plugins.lookup.csvfile as module_0

class Test_Csvfile_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            c_s_v_recoder_0 = module_0.CSVRecoder(bool_0)
            var_0 = c_s_v_recoder_0.__next__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
