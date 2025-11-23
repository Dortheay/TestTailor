import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'Jh.b[z-"2'
        str_1 = 'v2_runner_on_async_poll'
        bool_0 = False
        immutable_dict_0 = module_0.ImmutableDict()
        var_0 = immutable_dict_0.__eq__(bool_0)
        float_0 = -304.0
        str_2 = None
        dict_0 = {str_0: str_0, str_1: float_0, str_2: str_0, str_1: str_2, str_0: str_1}
        immutable_dict_1 = module_0.ImmutableDict()
        var_1 = module_0.is_iterable(dict_0, immutable_dict_1)

if __name__ == "__main__":
    unittest.main()
