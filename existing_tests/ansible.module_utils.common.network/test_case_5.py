import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            tuple_0 = ()
            dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0}
            var_0 = module_0.to_bits(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
