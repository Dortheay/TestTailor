import unittest
import timeout_decorator
import blib2to3.pgen2.pgen as module_0

class Test_Pgen_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        n_f_a_state_0 = module_0.NFAState()
        dict_0 = {n_f_a_state_0: n_f_a_state_0}
        d_f_a_state_0 = module_0.DFAState(dict_0, n_f_a_state_0)

if __name__ == "__main__":
    unittest.main()
