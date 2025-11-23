import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = 'cg0A#}\\[E=)Gl\x0c`/Ar/W'
            str_1 = module_0.reverse(str_0)
            str_2 = '\n    Convert the given number/string into a roman number.\n\n    The passed input must represents a positive integer in the range 1-3999 (inclusive).\n\n    Why this limit? You may be wondering:\n\n    1. zero is forbidden since there is no related representation in roman numbers\n    2. the upper bound 3999 is due to the limitation in the ascii charset    (the higher quantity sign displayable in ascii is "M" which is equal to 1000, therefore based on    roman numbers rules we can use 3 times M to reach 3000 but we can\'t go any further in thousands without    special "boxed chars").\n\n    *Examples:*\n\n    >>> roman_encode(37) # returns \'XXXVIII\'\n    >>> roman_encode(\'2020\') # returns \'MMXX\'\n\n    :param input_number: An integer or a string to be converted.\n    :type input_number: Union[str, int]\n    :return: Roman number string.\n    '
            str_3 = module_0.prettify(str_2)
            str_4 = module_0.roman_encode(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
