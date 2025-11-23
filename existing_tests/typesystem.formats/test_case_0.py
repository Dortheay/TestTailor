import unittest
import timeout_decorator
import typesystem.formats as module_0

class Test_Formats_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        date_format_0 = module_0.DateFormat()

if __name__ == "__main__":
    unittest.main()
