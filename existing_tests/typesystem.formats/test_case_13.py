import unittest
import timeout_decorator
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

class Test_Formats_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            u_u_i_d_format_0 = module_0.UUIDFormat()
            str_0 = '123e4567-e89b-12d3-a456-426614174000'
            u_u_i_d_0 = u_u_i_d_format_0.validate(str_0)
            u_u_i_d_1 = module_1.UUID(str_0)
            str_1 = '123e4567-e89b-12d3-a456-invalidUUID'
            u_u_i_d_2 = u_u_i_d_format_0.validate(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
