import unittest
import timeout_decorator
import typesystem.schemas as module_0
import typesystem.fields as module_1

class Test_Schemas_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '~\\Em@C/_!\x0cSk'
            reference_0 = module_0.Reference(str_0)
            any_0 = reference_0.validate(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
