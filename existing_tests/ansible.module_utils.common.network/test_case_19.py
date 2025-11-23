import unittest
import timeout_decorator
import ansible.module_utils.common.network as module_0

class Test_Network_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
        var_0 = module_0.to_ipv6_subnet(str_0)
        str_1 = '2001:0db8:85a3::8a2e:0370:7334'
        var_1 = module_0.to_ipv6_subnet(str_1)
        str_2 = '2001:0db8::'
        var_2 = module_0.to_ipv6_subnet(str_2)
        str_3 = '2001::'
        var_3 = module_0.to_ipv6_subnet(str_3)
        str_4 = '2001:0db8:85a3:invalid:0000:8a2e:0370:7334'
        var_4 = module_0.to_ipv6_subnet(str_4)
        str_5 = ''
        var_5 = module_0.to_ipv6_subnet(str_5)

if __name__ == "__main__":
    unittest.main()
