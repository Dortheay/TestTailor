import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'la$\\uX/+c6D'
        bytes_0 = b'\xd0O\x02\xfb \x0c\x82\xe6\x02\xf1\x12\x9f\xf4'
        validation_0 = module_0.Validation(str_0, bytes_0)
        str_1 = '(RI\t!"D6M'
        var_0 = validation_0.__eq__(str_1)
        var_1 = validation_0.to_maybe()

if __name__ == "__main__":
    unittest.main()
