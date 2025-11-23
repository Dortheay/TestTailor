import unittest
import timeout_decorator
import ansible.plugins.lookup.first_found as module_0

class Test_First_found_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\xc6\xe0\xf6\x81?\x05\xfb\xb5\x07'
            float_0 = 4956.35074
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.run(bytes_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
