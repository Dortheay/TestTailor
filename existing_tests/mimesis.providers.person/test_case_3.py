import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = None
            dict_0 = {}
            bool_0 = True
            person_0 = module_0.Person(**dict_0)
            var_0 = person_0.gender(bool_0)
            person_1 = module_0.Person()
            dict_1 = {str_0: str_0, str_0: dict_0, str_0: dict_0}
            person_2 = module_0.Person(**dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
