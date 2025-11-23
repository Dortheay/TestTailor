import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            person_0 = module_0.Person()
            str_0 = person_0.social_media_profile(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
