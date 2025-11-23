import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_49(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        var_0 = module_0.url_argument_spec()

if __name__ == "__main__":
    unittest.main()
