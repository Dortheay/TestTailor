import unittest
import timeout_decorator
import ansible.plugins.lookup.fileglob as module_0

class Test_Fileglob_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = ''
            lookup_module_0 = module_0.LookupModule(str_0)
            lookup_module_1 = module_0.LookupModule()
            int_0 = 257
            lookup_module_2 = module_0.LookupModule(str_0, int_0)
            bytes_0 = b'P7\xe9\x82 \xc0'
            tuple_0 = (bytes_0,)
            var_0 = lookup_module_0.run(tuple_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
