import unittest
import timeout_decorator
import apimd.loader as module_0

class Test_Loader_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'k/84'
        str_1 = '0!'
        dict_0 = {str_0: str_1}
        str_2 = 'typing.AsyncIterable'
        sequence_0 = module_0.gen_api(dict_0, str_1, prefix=str_2)

if __name__ == "__main__":
    unittest.main()
