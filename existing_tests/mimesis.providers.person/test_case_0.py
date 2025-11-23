import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = None
            person_0 = module_0.Person()
            int_1 = person_0.age(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
