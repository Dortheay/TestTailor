import unittest
import timeout_decorator
import dataclasses_json.mm as module_0

class Test_Mm_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            schema_f_0 = module_0.SchemaF()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
