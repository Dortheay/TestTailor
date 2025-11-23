import unittest
import timeout_decorator
import typesystem.base as module_0

class Test_Base_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            int_0 = -1417
            str_0 = ',\tyqIf}.fS&_nY\n"G>'
            set_0 = {str_0, int_0, int_0, str_0}
            base_error_0 = module_0.BaseError(text=str_0, code=str_0, position=set_0)
            list_0 = base_error_0.messages()
            int_1 = 4
            int_2 = 6
            position_0 = module_0.Position(int_0, int_2, int_0)
            str_1 = position_0.__repr__()
            position_1 = module_0.Position(int_0, int_1, int_1)
            bytes_0 = b'\x85\xa6\xa1^\x92\x80\x8e\xa0T\x81'
            base_error_1 = module_0.BaseError(text=position_1, messages=bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
