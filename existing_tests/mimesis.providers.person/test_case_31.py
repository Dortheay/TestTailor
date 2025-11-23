import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        dict_0 = {}
        person_0 = module_0.Person(**dict_0)
        str_0 = person_0.sexual_orientation()
        str_1 = person_0.email()
        gender_0 = module_1.Gender.MALE
        str_2 = person_0.surname(gender_0)
        str_3 = person_0.political_views()
        str_4 = person_0.political_views()
        person_1 = module_0.Person()
        str_5 = person_0.social_media_profile()
        str_6 = person_1.nationality()
        str_7 = person_0.nationality()
        var_0 = person_1.gender()
        person_2 = module_0.Person(**dict_0)
        str_8 = person_2.worldview()
        bool_0 = True
        str_9 = person_1.full_name(gender_0, bool_0)

if __name__ == "__main__":
    unittest.main()
