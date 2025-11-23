import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_38(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_37(self):
        try:
            str_0 = 'kB4g)=ktVwK58$}~\n1u'
            str_1 = "`k]F>'baV*_0\x0b"
            dict_0 = {str_0: str_0, str_1: str_1}
            list_0 = []
            var_0 = module_0.to_nice_yaml(dict_0, *list_0)
            var_1 = module_0.combine()
            list_1 = [list_0]
            var_2 = module_0.to_datetime(list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
