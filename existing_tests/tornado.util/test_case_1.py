import unittest
import timeout_decorator
import tornado.util as module_0
import builtins as module_1

class Test_Util_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            list_0 = []
            bytes_0 = b'\xf8Ng.\x85*d\xd5?\x81~\x19'
            str_0 = 'WwP91{Pl'
            object_dict_0 = module_0.ObjectDict(*list_0)
            object_dict_0.__setattr__(str_0, str_0)
            var_0 = module_0.timedelta_to_seconds(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
