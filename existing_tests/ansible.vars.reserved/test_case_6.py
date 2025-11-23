import unittest
import timeout_decorator
import ansible.vars.reserved as module_0

class Test_Reserved_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = -99.271545
            var_0 = module_0.get_reserved_names(float_0)
            var_1 = module_0.is_reserved_name(float_0)
            var_2 = module_0.get_reserved_names()
            float_1 = 3389.5
            var_3 = module_0.is_reserved_name(float_1)
            str_0 = '\x0bpy%PX&QeR'
            bytes_0 = b'9\x96\x81^\x8b\x87\x9d\x8d\xbey\x98\x04NR\x99'
            var_4 = module_0.warn_if_reserved(bytes_0)
            var_5 = module_0.get_reserved_names()
            var_6 = module_0.get_reserved_names()
            var_7 = module_0.is_reserved_name(str_0)
            str_1 = 'armv5tel'
            var_8 = module_0.warn_if_reserved(str_1, str_1)
            int_0 = 1996
            var_9 = module_0.is_reserved_name(int_0)
            int_1 = 81
            var_10 = module_0.warn_if_reserved(int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
