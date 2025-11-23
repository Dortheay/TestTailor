import unittest
import timeout_decorator
import dataclasses_json.mm as module_0

class Test_Mm_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = "l\tL'!Q8(yTatWZT~!^c\r"
            bool_0 = True
            iso_field_0 = module_0._IsoField()
            str_1 = 's?#\nl/h\'q&}%*&^"%yj'
            dict_0 = {str_1: bool_0, str_0: iso_field_0}
            str_2 = 'CatchAllVar'
            dict_1 = {str_2: str_2, str_2: bool_0, str_0: str_1}
            union_field_0 = module_0._UnionField(iso_field_0, dict_0, dict_1, **dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
