import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            filter_module_0 = module_0.FilterModule()
            str_0 = '5ZH'
            str_1 = '=&>_!,1'
            list_0 = [str_1, str_0]
            var_0 = module_0.to_uuid(list_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
