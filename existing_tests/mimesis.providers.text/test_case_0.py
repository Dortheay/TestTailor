import unittest
import timeout_decorator
import mimesis.providers.text as module_0

class Test_Text_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = {}
            text_0 = module_0.Text(**dict_0)
            list_0 = text_0.alphabet()
            tuple_0 = ()
            list_1 = [tuple_0, tuple_0, tuple_0, tuple_0]
            dict_1 = {}
            text_1 = module_0.Text(*list_1, **dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
