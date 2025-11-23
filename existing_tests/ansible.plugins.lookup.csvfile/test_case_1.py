import unittest
import timeout_decorator
import ansible.plugins.lookup.csvfile as module_0

class Test_Csvfile_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = 99
        c_s_v_recoder_0 = module_0.CSVRecoder(int_0)

if __name__ == "__main__":
    unittest.main()
