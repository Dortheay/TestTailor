import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        person_0 = module_0.Person()
        str_0 = person_0.username()
        person_1 = module_0.Person()
        str_1 = person_1.avatar()

if __name__ == "__main__":
    unittest.main()
