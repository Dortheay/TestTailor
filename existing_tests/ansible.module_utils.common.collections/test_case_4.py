import unittest
import timeout_decorator
import ansible.module_utils.common.collections as module_0

class Test_Collections_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bytes_0 = b''
            str_0 = 'sr)8t5(!^'
            float_0 = None
            list_0 = None
            dict_0 = {str_0: bytes_0, str_0: str_0, float_0: list_0, str_0: bytes_0}
            var_0 = module_0.count(dict_0)
            immutable_dict_0 = module_0.ImmutableDict()
            var_1 = immutable_dict_0.union(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
