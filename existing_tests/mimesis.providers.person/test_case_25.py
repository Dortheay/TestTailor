import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        person_0 = module_0.Person()
        str_0 = person_0.political_views()
        str_1 = person_0.worldview()

if __name__ == "__main__":
    unittest.main()
