import unittest
import timeout_decorator
import mimesis.providers.structure as module_0

class Test_Structure_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            structure_0 = module_0.Structure()
            str_0 = structure_0.html()
            str_1 = structure_0.html()
            str_2 = structure_0.html()
            str_3 = structure_0.css()
            str_4 = structure_0.html_attribute_value()
            list_0 = [str_4, str_2, structure_0]
            dict_0 = {}
            structure_1 = module_0.Structure(**dict_0)
            str_5 = structure_0.css_property()
            structure_2 = module_0.Structure(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
