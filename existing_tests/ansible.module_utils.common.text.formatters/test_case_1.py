import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'J?`iWrq75'
            var_0 = module_0.human_to_bytes(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
