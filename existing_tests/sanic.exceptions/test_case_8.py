import unittest
import timeout_decorator
import sanic.exceptions as module_0

class Test_Exceptions_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            list_0 = []
            var_0 = module_0.add_status_code(list_0)
            set_0 = set()
            tuple_0 = ()
            invalid_range_type_0 = module_0.InvalidRangeType(set_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
