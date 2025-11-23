import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.netbsd as module_0

class Test_Netbsd_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            tuple_0 = ()
            int_0 = 725
            net_b_s_d_hardware_0 = module_0.NetBSDHardware(int_0)
            var_0 = net_b_s_d_hardware_0.populate(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
