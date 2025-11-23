import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            time_0 = module_0.Time()
            bool_0 = True
            choice_0 = module_0.Choice()
            any_0 = choice_0.validate(time_0, strict=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
