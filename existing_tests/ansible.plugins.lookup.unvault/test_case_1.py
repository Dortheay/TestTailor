import unittest
import timeout_decorator
import ansible.plugins.lookup.unvault as module_0

class Test_Unvault_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'h\x01c\xce'
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.run(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
