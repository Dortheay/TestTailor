import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'qy'
        str_1 = module_0.doctest(str_0)
        str_2 = '\x0cq'
        str_3 = "z((lk\\/7'TjS~b^2?F("
        str_4 = '\rPQ+P4a6}J('
        dict_0 = {str_2: str_0, str_3: str_2, str_4: str_0, str_3: str_2}
        resolver_0 = module_0.Resolver(str_1, dict_0)

if __name__ == "__main__":
    unittest.main()
