import unittest
import timeout_decorator
import ansible.utils.py3compat as module_0

class Test_Py3compat_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = None
            dict_0 = {}
            text_environ_0 = module_0._TextEnviron()
            var_0 = text_environ_0.__setitem__(float_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
