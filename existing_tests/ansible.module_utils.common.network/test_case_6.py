import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = ',3vR\t{Tw={&m#"f+'
            var_0 = module_0.to_bits(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
