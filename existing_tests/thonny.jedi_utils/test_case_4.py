import unittest
import timeout_decorator
import thonny.jedi_utils as module_0

class Test_Jedi_utils_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'i#J9R!'
            int_0 = -191
            str_1 = '+h2f=z'
            var_0 = module_0.get_definitions(str_0, int_0, int_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
