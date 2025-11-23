import unittest
import timeout_decorator
import ansible.plugins.filter.urlsplit as module_0

class Test_Urlsplit_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'https://example.com:8080/path/to/resource?key=value#anchor'
        var_0 = module_0.split_url(str_0)
        str_1 = 'netloc'
        var_1 = module_0.split_url(str_0, str_1)
        var_2 = module_0.split_url(str_0, str_1)
        str_2 = 'http://example.com'
        var_3 = module_0.split_url(str_2)

if __name__ == "__main__":
    unittest.main()
