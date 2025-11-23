import unittest
import timeout_decorator
import mimesis.providers.text as module_0

class Test_Text_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = True
            text_0 = module_0.Text()
            tuple_0 = text_0.rgb_color(bool_0)
            int_0 = -4084
            text_1 = module_0.Text()
            str_0 = text_1.hex_color()
            bool_1 = True
            list_0 = text_1.alphabet(bool_1)
            list_1 = [int_0]
            str_1 = 'VH-nI/j'
            dict_0 = {str_1: list_1, str_1: list_1}
            text_2 = module_0.Text(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
