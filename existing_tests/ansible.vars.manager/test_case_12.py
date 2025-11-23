import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            bytes_0 = b'\x81!\xa1\x05'
            bytes_1 = b'\xfd\xdcp}\xe0\x83\x8a!\xec\xfb\x9a'
            float_0 = -3453.4965
            vars_with_sources_0 = module_0.VarsWithSources()
            var_0 = vars_with_sources_0.__setitem__(bytes_1, float_0)
            var_1 = module_0.preprocess_vars(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
