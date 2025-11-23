import unittest
import timeout_decorator
import mimesis.providers.structure as module_0

class Test_Structure_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            structure_0 = module_0.Structure()
            structure_1 = module_0.Structure()
            str_0 = structure_0.css_property()
            str_1 = structure_0.css_property()
            str_2 = structure_1.html_attribute_value()
            str_3 = structure_1.html_attribute_value(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
