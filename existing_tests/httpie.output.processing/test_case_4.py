import unittest
import timeout_decorator
import httpie.output.processing as module_0

class Test_Processing_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        list_0 = []
        dict_0 = {}
        formatting_0 = module_0.Formatting(list_0)
        formatting_1 = module_0.Formatting(list_0, **dict_0)
        str_0 = 'Uamy%'
        str_1 = formatting_1.format_headers(str_0)
        str_2 = 'o\rK~GP$023UQ:qy7f\t'
        str_3 = '!}D\nw7`=0'
        conversion_0 = module_0.Conversion()
        optional_0 = conversion_0.get_converter(str_1)
        str_4 = formatting_1.format_body(str_2, str_3)

if __name__ == "__main__":
    unittest.main()
