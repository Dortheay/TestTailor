import unittest
import timeout_decorator
import ansible.module_utils.splitter as module_0

class Test_Splitter_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '-.1^l'
            var_0 = module_0.split_args(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
