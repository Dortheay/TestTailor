import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.darwin as module_0

class Test_Darwin_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bytes_0 = b'\xdbt:\xed\xeb#\xd5hL~\xf0\xfe\xb7#\x16u\xab\x8c\t'
            set_0 = {bytes_0, bytes_0, bytes_0}
            darwin_hardware_0 = module_0.DarwinHardware(set_0)
            var_0 = darwin_hardware_0.get_memory_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
