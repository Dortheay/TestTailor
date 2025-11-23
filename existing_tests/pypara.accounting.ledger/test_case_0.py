import unittest
import timeout_decorator
import pypara.accounting.ledger as module_0

class Test_Ledger_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            general_ledger_program_0 = module_0.GeneralLedgerProgram()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
