import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            bool_0 = True
            person_0 = module_0.Person()
            str_0 = person_0.sexual_orientation(bool_0)
            str_1 = person_0.surname()
            float_0 = 2819.5321
            str_2 = person_0.university()
            str_3 = person_0.height(float_0, float_0)
            float_1 = 605.0
            str_4 = person_0.height(float_1)
            person_1 = module_0.Person()
            list_0 = [str_1, str_0]
            str_5 = person_0.full_name(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
