import unittest
import timeout_decorator
import blib2to3.pgen2.pgen as module_0

class Test_Pgen_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            n_f_a_state_0 = module_0.NFAState()
            str_0 = 'await'
            n_f_a_state_0.addarc(n_f_a_state_0)
            n_f_a_state_0.addarc(n_f_a_state_0)
            dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
            d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
            d_f_a_state_0.addarc(d_f_a_state_0, str_0)
            d_f_a_state_0.unifystate(d_f_a_state_0, d_f_a_state_0)
            d_f_a_state_0.addarc(d_f_a_state_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
