import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_51(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_50(self):
        try:
            str_0 = '\ng&c}4H`C'
            bool_0 = None
            str_1 = 'c9j!@zx~Yo\x0b=F|<=Z'
            bool_1 = True
            boolean_0 = module_0.Boolean(description=str_1, default=str_1, allow_null=bool_1)
            any_0 = boolean_0.validate(str_0, strict=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
