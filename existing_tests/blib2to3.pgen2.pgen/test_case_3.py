import unittest
import timeout_decorator
import blib2to3.pgen2.pgen as module_0

class Test_Pgen_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            n_f_a_state_0 = module_0.NFAState()
            str_0 = ')H\r_~aG'
            n_f_a_state_0.addarc(n_f_a_state_0, str_0)
            dict_0 = None
            str_1 = '.mI"Z'
            tuple_0 = (dict_0, str_1)
            n_f_a_state_0.addarc(n_f_a_state_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
