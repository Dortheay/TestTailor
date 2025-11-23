import unittest
import timeout_decorator
import ansible.utils._junit_xml as module_0

class Test__junit_xml_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = "RO\n3'<CZhn\r+9]C\x0bJ5Q"
        str_1 = '-*+~vaE'
        test_error_0 = module_0.TestError()
        list_0 = [test_error_0, test_error_0]
        bool_0 = False
        test_case_0 = module_0.TestCase(str_0, str_1, str_0, str_1, list_0, bool_0)
        dict_0 = test_case_0.get_attributes()

if __name__ == "__main__":
    unittest.main()
