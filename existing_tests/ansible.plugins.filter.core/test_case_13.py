import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            str_0 = 'S}/K6\r2&`H\x0cMMxu+\x0c'
            list_0 = [str_0, str_0, str_0]
            list_1 = [list_0, str_0]
            var_0 = module_0.combine(*list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
