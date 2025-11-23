import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        int_0 = -1506
        person_0 = module_0.Person()
        int_1 = person_0.weight(int_0)
        person_1 = module_0.Person()
        str_0 = '\n5"x.Xjp49\nLoUc'
        str_1 = person_1.telephone(str_0)
        str_2 = person_1.university()
        str_3 = person_0.views_on()

if __name__ == "__main__":
    unittest.main()
