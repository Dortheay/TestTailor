import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '5\n'
            list_0 = [str_0]
            register_0 = module_0.Register()
            dict_0 = register_0.as_dict()
            register_0.set_eightbit_call(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
