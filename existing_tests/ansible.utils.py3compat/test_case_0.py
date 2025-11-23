import unittest
import timeout_decorator
import ansible.utils.py3compat as module_0

class Test_Py3compat_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '3v'
            text_environ_0 = module_0._TextEnviron()
            var_0 = text_environ_0.__delitem__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
