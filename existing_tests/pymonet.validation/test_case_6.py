import unittest
import timeout_decorator
import pymonet.validation as module_0

class Test_Validation_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            int_0 = None
            list_0 = []
            str_0 = ')J_*>=r\x0cnFH.b@wm"Z>s'
            bytes_0 = b'dl\xb87\x92z'
            validation_0 = module_0.Validation(int_0, str_0)
            bytes_1 = b'\x1eH9\xd4\xeeV~\x04\x16\xe9\xd4\x0eG\x9c\t\x12\x90'
            validation_1 = module_0.Validation(validation_0, bytes_1)
            var_0 = validation_1.is_fail()
            str_1 = '\n        :param semigroup: other semigroup to concat\n        :type semigroup: Sum[B]\n        :returns: new Sum with sum of concat semigroups values\n        :rtype: Sum[A]\n        '
            dict_0 = {bytes_0: bytes_0, str_1: str_1, str_1: bytes_0}
            validation_2 = module_0.Validation(bytes_0, dict_0)
            validation_3 = module_0.Validation(list_0, str_0)
            validation_4 = module_0.Validation(validation_3, list_0)
            var_1 = validation_4.__eq__(int_0)
            var_2 = validation_4.__str__()
            bytes_2 = b'\x08p\xe7rw0\x80":\xba\x8c\xf2\xa33l\x92\xb3\xa0'
            set_0 = {bytes_2, bytes_2}
            validation_5 = module_0.Validation(list_0, list_0)
            var_3 = validation_5.to_box()
            float_0 = None
            bytes_3 = b'\r'
            str_2 = 'oIucfh3tL{t\rb_>(<'
            validation_6 = module_0.Validation(list_0, str_2)
            validation_7 = module_0.Validation(bytes_3, set_0)
            var_4 = validation_7.map(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
