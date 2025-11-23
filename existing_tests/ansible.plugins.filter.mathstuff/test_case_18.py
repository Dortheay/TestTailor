import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            int_0 = -569
            set_0 = {int_0, int_0}
            list_0 = []
            str_0 = "@<]BX' \tT<\t\x0b0M?"
            tuple_0 = (set_0, list_0, str_0, set_0)
            var_0 = module_1.power(tuple_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
