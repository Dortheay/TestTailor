import unittest
import timeout_decorator
import mimesis.providers.text as module_0

class Test_Text_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        bool_0 = False
        list_0 = [bool_0]
        text_0 = module_0.Text(*list_0)
        str_0 = text_0.color()
        text_1 = module_0.Text()
        str_1 = text_1.level()
        text_2 = module_0.Text()
        str_2 = text_2.answer()

if __name__ == "__main__":
    unittest.main()
