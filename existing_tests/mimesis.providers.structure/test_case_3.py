import unittest
import timeout_decorator
import mimesis.providers.structure as module_0

class Test_Structure_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            structure_0 = module_0.Structure()
            str_0 = structure_0.html()
            str_1 = structure_0.html()
            str_2 = structure_0.html_attribute_value(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
