import unittest
import timeout_decorator
import blib2to3.pgen2.pgen as module_0

class Test_Pgen_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            n_f_a_state_0 = module_0.NFAState()
            str_0 = 'Od61_fwC-(L'
            dict_0 = {n_f_a_state_0: n_f_a_state_0, n_f_a_state_0: str_0}
            d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
            n_f_a_state_1 = module_0.NFAState()
            n_f_a_state_2 = None
            d_f_a_state_1 = module_0.DFAState(dict_0, n_f_a_state_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
