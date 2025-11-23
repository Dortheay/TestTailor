import unittest
import timeout_decorator
import ansible.module_utils.urls as module_0

class Test_Urls_55(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        var_0 = module_0.url_argument_spec()
        bytes_0 = b'&2\xbb\xfath'
        var_1 = module_0.generic_urlparse(bytes_0)

if __name__ == "__main__":
    unittest.main()
