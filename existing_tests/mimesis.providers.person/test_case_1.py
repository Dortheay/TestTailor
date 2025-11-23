import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            person_0 = module_0.Person()
            str_0 = person_0.social_media_profile()
            int_0 = 3493
            int_1 = person_0.weight(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
