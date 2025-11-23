import unittest
import timeout_decorator
import mimesis.providers.text as module_0

class Test_Text_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        text_0 = module_0.Text()
        str_0 = text_0.hex_color()
        list_0 = text_0.words()
        str_1 = text_0.level()
        str_2 = text_0.swear_word()
        str_3 = text_0.color()
        text_1 = module_0.Text()
        str_4 = text_0.color()
        str_5 = text_1.quote()
        str_6 = text_1.sentence()
        int_0 = 476
        list_1 = text_1.words(int_0)

if __name__ == "__main__":
    unittest.main()
