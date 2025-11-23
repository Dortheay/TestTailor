import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        float_0 = -1850.26
        person_0 = module_0.Person()
        str_0 = person_0.height(float_0)

if __name__ == "__main__":
    unittest.main()
