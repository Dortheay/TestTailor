import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_38(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_37(self):
        try:
            str_0 = 'i\rLv{7UUQ;Q_+aB'
            number_0 = module_0.Number(precision=str_0)
            bool_0 = True
            any_0 = number_0.validate(str_0, strict=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
