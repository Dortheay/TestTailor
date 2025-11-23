import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        person_0 = module_0.Person()
        var_0 = person_0.gender()
        var_1 = person_0.sex()
        str_0 = person_0.blood_type()
        str_1 = person_0.username()
        str_2 = person_0.surname()

if __name__ == "__main__":
    unittest.main()
