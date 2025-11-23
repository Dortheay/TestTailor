import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        bool_0 = True
        person_0 = module_0.Person()
        str_0 = person_0.sexual_orientation(bool_0)
        float_0 = 2819.5321
        str_1 = person_0.height(float_0, float_0)
        float_1 = 605.0
        str_2 = person_0.height(float_1)
        person_1 = module_0.Person()
        var_0 = person_1.first_name()
        str_3 = person_1.nationality()

if __name__ == "__main__":
    unittest.main()
