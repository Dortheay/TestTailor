import unittest
import timeout_decorator
import blib2to3.pgen2.pgen as module_0

class Test_Pgen_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        n_f_a_state_0 = module_0.NFAState()
        n_f_a_state_1 = module_0.NFAState()
        n_f_a_state_1.addarc(n_f_a_state_0)

if __name__ == "__main__":
    unittest.main()
