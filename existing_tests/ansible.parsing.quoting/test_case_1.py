import unittest
import timeout_decorator
import ansible.parsing.quoting as module_0

class Test_Quoting_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '=8x}hM901ot"8K7]'
        dict_0 = {str_0: str_0}
        var_0 = module_0.unquote(dict_0)
        var_1 = module_0.unquote(str_0)

if __name__ == "__main__":
    unittest.main()
