import unittest
import timeout_decorator
import pypara.accounting.journaling as module_0

class Test_Journaling_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = '6neMoney'
        date_0 = None
        journal_entry_0 = module_0.JournalEntry(date_0, str_0, date_0)
        journal_entry_0.validate()

if __name__ == "__main__":
    unittest.main()
