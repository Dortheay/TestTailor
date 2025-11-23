import unittest
import timeout_decorator
import dataclasses_json.core as module_0

class Test_Core_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            field_override_0 = module_0.FieldOverride()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
