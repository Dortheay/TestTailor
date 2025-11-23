import unittest
import timeout_decorator
import ansible.utils.py3compat as module_0

class Test_Py3compat_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '0,\\Y0uw'
            text_environ_0 = module_0._TextEnviron(str_0)
            text_environ_1 = module_0._TextEnviron()
            var_0 = text_environ_0.__iter__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
