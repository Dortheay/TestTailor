import unittest
import timeout_decorator
import ansible.plugins.filter.urlsplit as module_0

class Test_Urlsplit_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'J:]!V(DE&@5*\tic~'
        var_0 = module_0.split_url(str_0)

if __name__ == "__main__":
    unittest.main()
