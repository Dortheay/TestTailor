import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'virtinfo'
            dict_0 = {str_0: str_0}
            var_0 = module_0.is_masklen(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
