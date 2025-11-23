import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bytes_0 = b'\x81\x89\xd7\xa1E\x02\x0eE\r\xbb\xc0'
            bool_0 = True
            set_0 = set()
            list_0 = [bytes_0, set_0, set_0]
            tuple_0 = ()
            var_0 = module_1.difference(bool_0, list_0, tuple_0)
            int_0 = 2801
            str_0 = 'w]iC2<nfqIjW [o58Pu'
            bool_1 = False
            var_1 = module_1.union(int_0, str_0, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
