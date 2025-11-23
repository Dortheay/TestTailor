import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bool_0 = True
        list_0 = []
        person_0 = module_0.Person(*list_0)
        str_0 = person_0.identifier()
        str_1 = person_0.username()
        person_1 = module_0.Person()
        var_0 = person_1.first_name()
        person_2 = module_0.Person()
        str_2 = person_2.password(bool_0)
        str_3 = person_2.worldview()

if __name__ == "__main__":
    unittest.main()
