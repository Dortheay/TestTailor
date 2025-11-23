import unittest
import timeout_decorator
import mimesis.providers.person as module_0
import mimesis.enums as module_1

class Test_Person_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        optional_0 = None
        person_0 = module_0.Person()
        str_0 = person_0.political_views()
        str_1 = person_0.full_name(optional_0)
        str_2 = 'application/vnd.oma.bcast.imd+xml'
        str_3 = '51"/K15\rHk:Z\tcu4T/j:'
        dict_0 = {str_2: str_0, str_0: str_1, str_3: optional_0}
        bool_0 = False
        social_network_0 = module_1.SocialNetwork.FACEBOOK
        tuple_0 = (dict_0, bool_0, social_network_0)
        str_4 = person_0.nationality(tuple_0)

if __name__ == "__main__":
    unittest.main()
