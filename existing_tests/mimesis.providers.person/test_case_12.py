import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        person_0 = module_0.Person()
        gender_0 = module_1.Gender.MALE
        str_0 = person_0.name(gender_0)
        str_1 = person_0.last_name()

if __name__ == "__main__":
    unittest.main()
