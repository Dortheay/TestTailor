import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = ';6Puny'
            dict_0 = {}
            var_0 = module_0.get_hash(str_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
