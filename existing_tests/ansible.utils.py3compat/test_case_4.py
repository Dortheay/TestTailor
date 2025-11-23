import unittest
import timeout_decorator
import ansible.utils.py3compat as module_0

class Test_Py3compat_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            float_0 = -996.913528
            text_environ_0 = module_0._TextEnviron(float_0)
            var_0 = text_environ_0.__delitem__(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
