import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        person_0 = module_0.Person()
        var_0 = person_0.first_name()
        person_1 = module_0.Person()
        str_0 = person_1.email()
        bool_0 = False
        int_0 = person_1.work_experience()
        str_1 = person_0.surname()
        person_2 = module_0.Person()
        gender_0 = module_1.Gender.FEMALE
        social_network_0 = module_1.SocialNetwork.VK
        list_0 = [bool_0, person_2, social_network_0, int_0]
        str_2 = ' )?nFH^".CtA8\x0cb\n&6v'
        tuple_0 = (gender_0, list_0, str_2)
        str_3 = person_0.email(tuple_0)
        str_4 = person_1.identifier()
        str_5 = person_1.name()
        str_6 = person_1.blood_type()
        str_7 = person_0.occupation()

if __name__ == "__main__":
    unittest.main()
