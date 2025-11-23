import unittest
import timeout_decorator
import mimesis.providers.text as module_0

class Test_Text_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = -3085
        text_0 = module_0.Text()
        str_0 = text_0.level()
        bool_0 = False
        tuple_0 = text_0.rgb_color(bool_0)
        str_1 = text_0.text(int_0)

if __name__ == "__main__":
    unittest.main()
