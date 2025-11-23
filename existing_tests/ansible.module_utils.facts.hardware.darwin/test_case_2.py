import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.darwin as module_0

class Test_Darwin_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = ''
            bytes_0 = b'\x98\xe7'
            darwin_hardware_0 = module_0.DarwinHardware(str_0, bytes_0)
            var_0 = darwin_hardware_0.get_system_profile()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
