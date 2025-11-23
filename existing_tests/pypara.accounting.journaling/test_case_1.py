import unittest
import timeout_decorator
import pypara.accounting.journaling as module_0

class Test_Journaling_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            date_0 = None
            str_0 = 'on\rMoney'
            journal_entry_0 = module_0.JournalEntry(date_0, str_0, date_0)
            account_0 = None
            bytes_0 = b'\x8a\x12|90p[A\x93\x84\xf1\xc8\xbc\xa3'
            var_0 = journal_entry_0.post(date_0, account_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
