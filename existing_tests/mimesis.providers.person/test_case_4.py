import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'video/vnd.CCTV'
            str_1 = '%3f5_6@t!'
            str_2 = '17Z sa'
            str_3 = ''
            dict_0 = {str_0: str_0, str_1: str_1, str_2: str_1, str_3: str_3}
            person_0 = module_0.Person()
            str_4 = person_0.academic_degree()
            person_1 = module_0.Person(**dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
