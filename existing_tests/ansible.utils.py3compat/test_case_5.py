import unittest
import timeout_decorator
import ansible.utils.py3compat as module_0

class Test_Py3compat_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        text_environ_0 = module_0._TextEnviron()

if __name__ == "__main__":
    unittest.main()
