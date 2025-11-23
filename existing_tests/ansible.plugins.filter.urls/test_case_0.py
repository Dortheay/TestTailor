import unittest
import timeout_decorator
import ansible.plugins.filter.urls as module_0

class Test_Urls_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        filter_module_0 = module_0.FilterModule()

if __name__ == "__main__":
    unittest.main()
