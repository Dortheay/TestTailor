import unittest
import timeout_decorator
import blib2to3.pgen2.pgen as module_0

class Test_Pgen_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        n_f_a_state_0 = module_0.NFAState()
        str_0 = 'Od61_fC-(L'
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: str_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        n_f_a_state_1 = module_0.NFAState()
        dict_1 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_1, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_1 = module_0.DFAState(dict_1, n_f_a_state_0)
        d_f_a_state_1.addarc(d_f_a_state_0, str_0)
        n_f_a_state_2 = module_0.NFAState()
        n_f_a_state_2.addarc(n_f_a_state_0)
        bool_0 = d_f_a_state_1.__eq__(d_f_a_state_0)

if __name__ == "__main__":
    unittest.main()
