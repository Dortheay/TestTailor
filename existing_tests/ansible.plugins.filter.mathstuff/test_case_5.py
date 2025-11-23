import unittest
import timeout_decorator
import ansible.plugins.filter.mathstuff as module_0

class Test_Mathstuff_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        bytes_0 = b'\x81\x89\xd7\xa1E\x02\x0eE\r\xbb\xc0'
        bool_0 = True
        set_0 = set()
        filter_module_0 = module_0.FilterModule()
        var_0 = filter_module_0.filters()
        list_0 = [bytes_0, set_0, set_0]
        tuple_0 = ()
        var_1 = module_0.difference(bool_0, list_0, tuple_0)

if __name__ == "__main__":
    unittest.main()
