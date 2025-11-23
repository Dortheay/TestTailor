import unittest
import timeout_decorator
import blib2to3.pgen2.pgen as module_0

class Test_Pgen_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            n_f_a_state_0 = module_0.NFAState()
            dict_0 = {n_f_a_state_0: n_f_a_state_0}
            d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)
            n_f_a_state_1 = None
            dict_1 = {n_f_a_state_1: n_f_a_state_1, n_f_a_state_1: n_f_a_state_1}
            d_f_a_state_1 = module_0.DFAState(dict_1, n_f_a_state_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
