import unittest
import timeout_decorator
import pytutils.env as module_0

class Test_Env_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            iterable_0 = None
            ordered_dict_0 = module_0.load_env_file(iterable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
