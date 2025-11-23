import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            register_0 = module_0.Register()
            register_1 = register_0.copy()
            register_2 = register_1.copy()
            register_2.unmute()
            bytes_0 = b'8\xda\\\x87\xde\xd2\xc74\xcel)\xef\x0b0\xca,Y\xd1\x12\xb8'
            list_0 = []
            str_0 = register_2.__call__(*list_0)
            set_0 = {bytes_0, register_2, register_0}
            register_2.set_rgb_call(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
