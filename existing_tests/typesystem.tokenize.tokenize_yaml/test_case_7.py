import unittest
import timeout_decorator
import typesystem.tokenize.tokenize_yaml as module_0
import typesystem.fields as module_1

class Test_Tokenize_yaml_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'\x91\x88$|\xd3\xa5s\x8f\xe95\x8c\xd83\x81\xaa\x07'
            field_0 = module_1.Field()
            any_0 = module_0.validate_yaml(bytes_0, field_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
