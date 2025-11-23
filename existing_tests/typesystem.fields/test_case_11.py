import unittest
import timeout_decorator
import typesystem.fields as module_0
import decimal as module_1

class Test_Fields_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            bytes_0 = b'\xdb\xda\xa1\xdf\xbd\xb5&}/\x81\x96'
            str_0 = 'N'
            boolean_0 = module_0.Boolean(title=str_0)
            any_0 = boolean_0.validate(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
