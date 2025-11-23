import unittest
import timeout_decorator
import ansible.utils.version as module_0

class Test_Version_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = '~;AKLyJ]'
            list_0 = []
            alpha_0 = module_0._Alpha(list_0)
            var_0 = alpha_0.__gt__(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
