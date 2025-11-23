import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        dict_0 = {}
        person_0 = module_0.Person(**dict_0)
        str_0 = person_0.sexual_orientation()
        str_1 = person_0.political_views()
        str_2 = person_0.political_views()
        person_1 = module_0.Person()
        str_3 = person_0.social_media_profile()
        str_4 = person_1.nationality()
        var_0 = person_1.gender()
        int_0 = person_0.work_experience()
        str_5 = person_0.password()
        person_2 = module_0.Person(**dict_0)
        var_1 = person_1.first_name()
        person_3 = module_0.Person()

if __name__ == "__main__":
    unittest.main()
