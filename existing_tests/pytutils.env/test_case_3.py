import unittest
import timeout_decorator
import pytutils.env as module_0

class Test_Env_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'class'
        str_1 = module_0.expand(str_0)

if __name__ == "__main__":
    unittest.main()
