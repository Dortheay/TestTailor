import unittest
import timeout_decorator
import ansible.plugins.filter.urls as module_0

class Test_Urls_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = '8`<gU<qc00ZeHbnt'
        var_0 = module_0.do_urlencode(str_0)
        list_0 = []
        var_1 = module_0.do_urlencode(list_0)

if __name__ == "__main__":
    unittest.main()
