import unittest
import timeout_decorator
import ansible.plugins.lookup.together as module_0

class Test_Together_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'P\x19\xb0C\xaf5\x87\x8fn\xce[\x1d\xc8d\xfd'
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.run(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
