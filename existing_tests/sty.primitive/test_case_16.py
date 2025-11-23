import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            register_0 = module_0.Register()
            register_1 = register_0.copy()
            register_2 = register_1.copy()
            register_2.unmute()
            str_0 = '\n        Use this method to unmute a previously muted register object.\n        '
            list_0 = [str_0]
            str_1 = register_2.__call__(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
