import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = '\n    This is a HP-UX specific subclass of Virtual. It defines\n    - virtualization_type\n    - virtualization_role\n    '
            var_0 = module_0.to_ipv6_subnet(str_0)
            str_1 = "\tJ:LnT'-}!!a:Xv36j"
            var_1 = module_0.to_ipv6_network(str_1)
            bool_0 = True
            str_2 = '})Xf6tyST|l2C@n'
            var_2 = module_0.to_ipv6_network(str_2)
            var_3 = module_0.to_netmask(bool_0)
            bytes_0 = b'?Eo\xd6\xde\t)X\xf0\xa1\n\xc4\x1d\xce\xc8\xda\xbd\x8eY\xe5'
            float_0 = 512.0
            var_4 = module_0.to_subnet(bytes_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
