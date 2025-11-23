import unittest
import timeout_decorator
import sanic.blueprint_group as module_0

class Test_Blueprint_group_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'p;'
            dict_0 = {str_0: str_0}
            bytes_0 = b'e\xe8\x82\xa9\x0f\xa9\xe6D\xe0V\xae\x13\xa9\xb7\xfc@'
            blueprint_group_0 = module_0.BlueprintGroup(bytes_0)
            blueprint_group_0.__setitem__(str_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
