import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '})Xf6ty{ST|U2C@n'
            var_0 = module_0.to_subnet(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
