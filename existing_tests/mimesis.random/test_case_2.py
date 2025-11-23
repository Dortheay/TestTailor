import unittest
import timeout_decorator
import mimesis.random as module_0

class Test_Random_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'nontarred'
        random_0 = module_0.Random()
        int_0 = 1861
        list_0 = random_0.randints(int_0)
        str_1 = random_0.custom_code(str_0)

if __name__ == "__main__":
    unittest.main()
