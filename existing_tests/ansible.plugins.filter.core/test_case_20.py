import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            bytes_0 = b''
            float_0 = 512.0
            var_0 = module_0.flatten(bytes_0, float_0)
            filter_module_0 = module_0.FilterModule()
            var_1 = module_0.path_join(filter_module_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
