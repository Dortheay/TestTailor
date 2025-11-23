import unittest
import timeout_decorator
import ansible.module_utils.facts.virtual.sunos as module_0

class Test_Sunos_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\x89\x81\x9e\xd4\xde\xed\xc5}\xfe\xbbQi\xef'
            sun_o_s_virtual_0 = module_0.SunOSVirtual(bytes_0)
            var_0 = sun_o_s_virtual_0.get_virtual_facts()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
