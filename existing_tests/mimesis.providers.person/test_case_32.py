import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        person_0 = module_0.Person()
        str_0 = person_0.nationality()
        list_0 = []
        bool_0 = True
        str_1 = person_0.email(list_0, bool_0)
        var_0 = person_0.gender()

if __name__ == "__main__":
    unittest.main()
