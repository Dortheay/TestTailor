import unittest
import timeout_decorator
import dataclasses_json.mm as module_0

class Test_Mm_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            list_0 = []
            str_0 = "Received input field with same name as catch-all field: '"
            str_1 = 'O="-\n'
            dict_0 = {str_0: list_0, str_1: str_1, str_1: list_0}
            bool_0 = True
            timestamp_field_0 = module_0._TimestampField(load_only=bool_0)
            var_0 = module_0.build_type(list_0, dict_0, timestamp_field_0, timestamp_field_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
