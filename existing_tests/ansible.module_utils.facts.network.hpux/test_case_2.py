import unittest
import timeout_decorator
import ansible.module_utils.facts.network.hpux as module_0

class Test_Hpux_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'\x1c.K\xc5|\x91\xb3\x16\x83G0'
            list_0 = []
            h_p_u_x_network_0 = module_0.HPUXNetwork(bytes_0, list_0)
            var_0 = h_p_u_x_network_0.get_interfaces_info()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
