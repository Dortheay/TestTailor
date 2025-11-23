import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            person_0 = module_0.Person()
            str_0 = person_0.telephone()
            str_1 = '\\nJwa\t@'
            dict_0 = {str_1: str_1}
            str_2 = person_0.nationality()
            person_1 = module_0.Person(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
