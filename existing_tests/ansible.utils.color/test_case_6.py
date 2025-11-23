import unittest
import timeout_decorator
import ansible.utils.color as module_0

class Test_Color_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '0y<Oz'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        var_0 = module_0.colorize(dict_0, dict_0, str_0)

if __name__ == "__main__":
    unittest.main()
