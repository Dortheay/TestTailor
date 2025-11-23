import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_47(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_46(self):
        try:
            date_time_0 = module_0.DateTime()
            dict_0 = {date_time_0: date_time_0, date_time_0: date_time_0}
            decimal_0 = module_1.Decimal()
            bool_0 = True
            string_0 = module_0.String(trim_whitespace=bool_0, pattern=dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
