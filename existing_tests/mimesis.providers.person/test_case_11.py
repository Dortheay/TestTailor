import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        person_0 = module_0.Person()
        str_0 = person_0.email()
        int_0 = person_0.work_experience()
        str_1 = person_0.surname()
        str_2 = person_0.identifier()
        var_0 = person_0.sex()
        str_3 = person_0.last_name()
        str_4 = person_0.language()

if __name__ == "__main__":
    unittest.main()
