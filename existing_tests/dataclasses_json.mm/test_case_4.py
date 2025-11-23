import unittest
import timeout_decorator
import dataclasses_json.mm as module_0

class Test_Mm_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            bool_0 = True
            bytes_0 = b'[J\xfadno\xd4\x93y\x00\x0e\xfbo\xd7\xd5\xd2\x89'
            float_0 = 1892.052
            tuple_0 = (bytes_0, float_0)
            str_0 = '4c"WS1qv/wSp1!bSCZ('
            str_1 = "Ja\x0c,'N\rrsyLWMzT]a3$J"
            str_2 = '#d\to1o-zN^T2@H\x0c\\['
            str_3 = 'dumps'
            str_4 = ' detected in '
            dict_0 = {str_0: str_0, str_1: str_2, str_3: str_4, str_4: str_4}
            iso_field_0 = module_0._IsoField(attribute=str_2, validate=dict_0, load_only=bool_0, dump_only=bool_0)
            type_0 = module_0.build_schema(bool_0, tuple_0, dict_0, iso_field_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
