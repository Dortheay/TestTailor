import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        dict_0 = {}
        person_0 = module_0.Person(**dict_0)
        str_0 = person_0.email()
        gender_0 = module_1.Gender.MALE
        str_1 = person_0.surname(gender_0)
        str_2 = person_0.political_views()
        str_3 = person_0.political_views()
        person_1 = module_0.Person()
        str_4 = person_0.social_media_profile()
        str_5 = person_1.nationality()
        var_0 = person_1.gender()
        int_0 = person_0.work_experience()
        int_1 = person_1.weight(int_0, int_0)
        person_2 = module_0.Person(**dict_0)
        str_6 = person_2.worldview()
        str_7 = person_0.full_name()

if __name__ == "__main__":
    unittest.main()
