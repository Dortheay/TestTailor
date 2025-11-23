import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        person_0 = module_0.Person()
        var_0 = person_0.first_name()
        person_1 = module_0.Person()
        str_0 = person_1.email()
        int_0 = person_1.work_experience()
        str_1 = person_1.surname()
        person_2 = module_0.Person()
        str_2 = person_1.identifier()
        str_3 = person_1.name()
        str_4 = person_1.blood_type()
        str_5 = person_1.occupation()

if __name__ == "__main__":
    unittest.main()
