import unittest
import timeout_decorator
import blib2to3.pgen2.pgen as module_0

class Test_Pgen_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        n_f_a_state_0 = module_0.NFAState()
        str_0 = 'await'
        n_f_a_state_0.addarc(n_f_a_state_0)
        n_f_a_state_0.addarc(n_f_a_state_0)
        dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
        d_f_a_state_0.addarc(d_f_a_state_0, str_0)
        d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_0)
        str_1 = ',,5_y!Rz}v'
        d_f_a_state_1.addarc(d_f_a_state_0, str_1)
        n_f_a_state_0.addarc(n_f_a_state_0)
        bool_0 = d_f_a_state_0.__eq__(d_f_a_state_1)

if __name__ == "__main__":
    unittest.main()
