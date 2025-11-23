import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_67(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_66(self):
        try:
            date_time_0 = module_0.DateTime()
            number_0 = module_0.Number(multiple_of=date_time_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
