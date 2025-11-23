import unittest
import timeout_decorator
import ansible.plugins.filter.urls as module_0

class Test_Urls_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '|,UkCOiWS\\LUs&\naj'
        var_0 = module_0.do_urldecode(str_0)

if __name__ == "__main__":
    unittest.main()
