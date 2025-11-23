import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            person_0 = module_0.Person()
            str_0 = person_0.social_media_profile()
            var_0 = person_0.first_name()
            person_1 = module_0.Person()
            str_1 = person_1.email()
            bool_0 = False
            int_0 = person_1.work_experience()
            str_2 = person_1.surname()
            person_2 = module_0.Person()
            str_3 = person_2.identifier()
            str_4 = person_1.name()
            str_5 = person_0.full_name(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
