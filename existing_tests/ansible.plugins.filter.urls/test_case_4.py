import unittest
import timeout_decorator
import ansible.plugins.filter.urls as module_0

class Test_Urls_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '8`<gU<qc00ZeHbnt'
        var_0 = module_0.do_urlencode(str_0)

if __name__ == "__main__":
    unittest.main()
