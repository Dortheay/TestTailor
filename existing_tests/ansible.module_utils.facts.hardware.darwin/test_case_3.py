import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.darwin as module_0

class Test_Darwin_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'x\xfc\xce'
            str_0 = '\nrg\nd<_Wp%:~'
            darwin_hardware_0 = module_0.DarwinHardware(bytes_0, str_0)
            var_0 = darwin_hardware_0.get_mac_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
