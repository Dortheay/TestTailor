import unittest
import timeout_decorator
import ansible.module_utils.facts.network.sunos as module_0

class Test_Sunos_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            list_0 = []
            str_0 = 'WGgd(u5D?KCX vGx'
            sun_o_s_network_0 = module_0.SunOSNetwork(str_0)
            var_0 = sun_o_s_network_0.get_interfaces_info(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
