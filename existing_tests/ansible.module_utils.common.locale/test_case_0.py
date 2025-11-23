import unittest
import timeout_decorator
import ansible.module_utils.common.locale as module_0

class Test_Locale_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'6s\x16\xe2-\xe9\xe3N#\x7f\xd1Q'
            var_0 = module_0.get_best_parsable_locale(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
