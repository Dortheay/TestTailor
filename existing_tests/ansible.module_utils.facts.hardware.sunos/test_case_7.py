import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.sunos as module_0

class Test_Sunos_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bytes_0 = b'\x82\xfa\xff\xe8\xb7{\xba\xa1O\xac\xdf\xda\x81\xa5\x82\x954H\xa0'
            bytes_1 = b'\x06}\xdd\xc1\x12\xdc\x82*\xf5\xad\ry$1\xd25'
            list_0 = [bytes_0]
            bool_0 = True
            tuple_0 = (list_0, bool_0)
            sun_o_s_hardware_collector_0 = module_0.SunOSHardwareCollector(tuple_0)
            sun_o_s_hardware_0 = module_0.SunOSHardware(sun_o_s_hardware_collector_0)
            var_0 = sun_o_s_hardware_0.get_cpu_facts(bytes_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
