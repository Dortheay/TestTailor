import unittest
import timeout_decorator
import httpie.utils as module_0

class Test_Utils_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'example.txt'
        var_0 = module_0.get_content_type(str_0)
        str_1 = 'example.gz'
        var_1 = module_0.get_content_type(str_1)
        str_2 = ''
        var_2 = module_0.get_content_type(str_2)
        str_3 = 'archive.tar.gz'
        var_3 = module_0.get_content_type(str_3)

if __name__ == "__main__":
    unittest.main()
