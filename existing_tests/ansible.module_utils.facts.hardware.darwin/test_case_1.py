import unittest
import timeout_decorator
import ansible.module_utils.facts.hardware.darwin as module_0

class Test_Darwin_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\x96{{\xe5\xb4\xdc\x19\xfe\xfc\xa2\x85:\x96\xbej\x8b\x1cj\xbb\x96'
            darwin_hardware_0 = module_0.DarwinHardware(bytes_0)
            var_0 = darwin_hardware_0.populate()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
