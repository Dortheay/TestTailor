import unittest
import timeout_decorator
import dataclasses_json.mm as module_0

class Test_Mm_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '\n        Return the parameters that will be written to the output dict\n        '
            dict_0 = {str_0: str_0}
            var_0 = module_0.schema(dict_0, str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
