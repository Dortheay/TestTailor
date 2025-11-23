import unittest
import timeout_decorator
import mimesis.providers.text as module_0

class Test_Text_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        text_0 = module_0.Text()
        list_0 = text_0.words()
        tuple_0 = text_0.rgb_color()
        text_1 = module_0.Text()
        text_2 = module_0.Text()
        str_0 = text_2.title()
        str_1 = text_1.sentence()
        str_2 = text_1.answer()
        text_3 = module_0.Text()
        str_3 = text_1.color()
        str_4 = text_0.sentence()
        str_5 = text_1.word()
        int_0 = -2148
        str_6 = text_3.text(int_0)
        dict_0 = {}
        text_4 = module_0.Text(**dict_0)
        str_7 = text_4.title()
        bool_0 = True
        str_8 = text_0.hex_color(bool_0)
        list_1 = text_1.words()

if __name__ == "__main__":
    unittest.main()
