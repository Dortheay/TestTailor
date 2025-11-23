import unittest
import timeout_decorator
import typesystem.composites as module_0
import typesystem.fields as module_1

class Test_Composites_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            set_0 = set()
            list_0 = []
            one_of_0 = module_0.OneOf(list_0)
            any_0 = one_of_0.validate(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
