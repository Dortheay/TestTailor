import unittest
import timeout_decorator
import ansible.plugins.lookup.first_found as module_0

class Test_First_found_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            lookup_module_0 = module_0.LookupModule()
            bytes_0 = b''
            float_0 = 3105.38
            list_0 = [bytes_0, float_0, bytes_0, lookup_module_0]
            var_0 = lookup_module_0.run(list_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
