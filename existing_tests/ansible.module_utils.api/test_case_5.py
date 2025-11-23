import unittest
import timeout_decorator
import ansible.module_utils.api as module_0

class Test_Api_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            tuple_0 = None
            list_0 = [tuple_0, tuple_0, tuple_0]
            set_0 = None
            bool_0 = True
            var_0 = module_0.retry_with_delays_and_condition(bool_0, bool_0)
            var_1 = module_0.retry_with_delays_and_condition(set_0)
            int_0 = 23
            var_2 = module_0.retry_never(tuple_0)
            var_3 = module_0.retry_never(int_0)
            var_4 = module_0.retry_argument_spec(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
