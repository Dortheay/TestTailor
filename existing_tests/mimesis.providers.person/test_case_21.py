import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        dict_0 = {}
        person_0 = module_0.Person(**dict_0)
        str_0 = person_0.surname()
        int_0 = 929
        person_1 = module_0.Person()
        int_1 = person_1.weight(int_0, int_0)

if __name__ == "__main__":
    unittest.main()
