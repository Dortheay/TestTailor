import unittest
import timeout_decorator
import ansible.utils.py3compat as module_0

class Test_Py3compat_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            int_0 = 126
            dict_0 = {int_0: int_0}
            text_environ_0 = module_0._TextEnviron()
            var_0 = text_environ_0.__len__()
            int_1 = -1295
            bool_0 = False
            text_environ_1 = module_0._TextEnviron(bool_0)
            var_1 = text_environ_1.__setitem__(dict_0, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
