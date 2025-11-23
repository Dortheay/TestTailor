import unittest
import timeout_decorator
import ansible.modules.subversion as module_0

class Test_Subversion_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = False
            float_0 = 442.698702
            int_0 = -1787
            str_0 = '0qX)?'
            str_1 = '>'
            str_2 = "}'62C"
            list_0 = []
            subversion_0 = module_0.Subversion(int_0, bool_0, str_0, str_1, str_2, bool_0, float_0, list_0)
            var_0 = subversion_0.get_revision()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
