import unittest
import timeout_decorator
import mimesis.providers.text as module_0

class Test_Text_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        dict_0 = {}
        text_0 = module_0.Text(**dict_0)
        str_0 = text_0.sentence()

if __name__ == "__main__":
    unittest.main()
