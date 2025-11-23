import unittest
import timeout_decorator
import apimd.loader as module_0

class Test_Loader_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'qy'
            str_1 = 'typing.AsyncIterable'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_1}
            int_0 = 1585
            sequence_0 = module_0.gen_api(dict_0, level=int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
