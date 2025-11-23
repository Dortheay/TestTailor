import unittest
import timeout_decorator
import ansible.utils.display as module_0
import ansible.plugins.filter.mathstuff as module_1

class Test_Mathstuff_36(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        try:
            str_0 = 'Ii'
            list_0 = [str_0]
            int_0 = -170
            bytes_0 = b'4/\xb4D\xdc\x83\xedJ\x7f\xcc<\x0e'
            bytes_1 = b'\xf1sm\xb9\xcf\x9f\x9a\xacr\x12'
            bool_0 = True
            tuple_0 = (bytes_1, bool_0)
            float_0 = -2781.796
            bool_1 = True
            tuple_1 = (tuple_0, float_0, bool_1)
            var_0 = module_1.symmetric_difference(int_0, bytes_0, tuple_1)
            var_1 = module_1.rekey_on_member(list_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
