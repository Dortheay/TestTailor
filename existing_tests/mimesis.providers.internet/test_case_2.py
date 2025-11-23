import unittest
import timeout_decorator
import mimesis.providers.internet as module_0
import mimesis.enums as module_1

class Test_Internet_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            int_0 = -492
            list_0 = []
            dict_0 = {}
            internet_0 = module_0.Internet(*list_0, **dict_0)
            str_0 = internet_0.image_placeholder(int_0)
            list_1 = [bool_0]
            list_2 = [list_1, list_1]
            internet_1 = module_0.Internet(*list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
