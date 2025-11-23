import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = "U%{&)[nLkal65*'y"
            bytes_0 = b'J\xbdF\xb6\xd2kb\x8fN\xbd\x81\xbb\xee\x98\x11\x0e\x94'
            filter_module_0 = module_1.FilterModule()
            var_0 = module_1.human_readable(str_0, bytes_0, filter_module_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
