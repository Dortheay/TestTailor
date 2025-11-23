import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            filter_module_0 = module_1.FilterModule()
            list_0 = None
            var_0 = module_1.human_to_bytes(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
