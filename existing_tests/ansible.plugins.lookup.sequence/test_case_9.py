import unittest
import timeout_decorator
import ansible.plugins.lookup.sequence as module_0

class Test_Sequence_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            dict_0 = {}
            lookup_module_0 = module_0.LookupModule(**dict_0)
            str_0 = '0,iI L)W!XZn-{>'
            dict_1 = {lookup_module_0: lookup_module_0, str_0: dict_0}
            var_0 = lookup_module_0.run(str_0, dict_1, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
