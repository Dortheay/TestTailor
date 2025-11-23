import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = '[a>h=#9\rxqYt%b{WcsA'
            float_0 = 1.0
            var_0 = module_0.map_structure(str_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
