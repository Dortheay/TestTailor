import unittest
import timeout_decorator
import sanic.utils as module_0
import pathlib as module_1
import _frozen_importlib_external as module_2

class Test_Utils_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'yes'
            bool_0 = module_0.str_to_bool(str_0)
            str_1 = 'YES'
            bool_1 = module_0.str_to_bool(str_1)
            str_2 = 'True'
            bool_2 = module_0.str_to_bool(str_2)
            str_3 = 't'
            bool_3 = module_0.str_to_bool(str_3)
            str_4 = 'on'
            bool_4 = module_0.str_to_bool(str_4)
            str_5 = '1'
            bool_5 = module_0.str_to_bool(str_5)
            str_6 = 'no'
            bool_6 = module_0.str_to_bool(str_6)
            str_7 = 'NO'
            bool_7 = module_0.str_to_bool(str_7)
            str_8 = 'False'
            bool_8 = module_0.str_to_bool(str_8)
            str_9 = 'f'
            bool_9 = module_0.str_to_bool(str_9)
            str_10 = 'off'
            bool_10 = module_0.str_to_bool(str_10)
            str_11 = '0'
            bool_11 = module_0.str_to_bool(str_11)
            str_12 = 'invalid'
            bool_12 = module_0.str_to_bool(str_12)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
