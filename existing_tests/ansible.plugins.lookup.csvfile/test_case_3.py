import unittest
import timeout_decorator
import ansible.plugins.lookup.csvfile as module_0

class Test_Csvfile_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bytes_0 = b'\xe7h\xb7\xbe4RD\xc4Aq\xa3\x89\xa2\xda\xcf\x90'
        int_0 = 1375
        c_s_v_reader_0 = module_0.CSVReader(bytes_0, int_0)

if __name__ == "__main__":
    unittest.main()
