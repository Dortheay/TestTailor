import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            time_0 = module_0.Time()
            field_0 = module_0.Field()
            any_0 = field_0.serialize(time_0)
            list_0 = None
            union_0 = module_0.Union(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
