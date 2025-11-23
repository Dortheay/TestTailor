import unittest
import timeout_decorator
import ansible.utils.helpers as module_0

class Test_Helpers_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'\xa5\x02'
            bool_0 = True
            tuple_0 = (bool_0, bool_0)
            var_0 = module_0.deduplicate_list(tuple_0)
            dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
            var_1 = module_0.pct_to_int(bytes_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
