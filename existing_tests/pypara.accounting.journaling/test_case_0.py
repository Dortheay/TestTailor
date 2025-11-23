import unittest
import timeout_decorator
import pypara.accounting.journaling as module_0

class Test_Journaling_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            read_journal_entries_0 = module_0.ReadJournalEntries()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
