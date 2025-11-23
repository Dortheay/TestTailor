import unittest
import timeout_decorator
import mimesis.providers.text as module_0

class Test_Text_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        text_0 = module_0.Text()
        list_0 = text_0.words()
        tuple_0 = text_0.rgb_color()
        text_1 = module_0.Text()
        text_2 = module_0.Text()
        str_0 = text_2.title()
        str_1 = text_1.sentence()
        text_3 = module_0.Text()
        str_2 = text_1.color()
        str_3 = text_0.sentence()
        str_4 = text_1.word()
        list_1 = text_1.alphabet()
        str_5 = text_1.title()

if __name__ == "__main__":
    unittest.main()
