import unittest
import timeout_decorator
import ansible.module_utils.splitter as module_0

class Test_Splitter_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = "'"
        var_0 = module_0.unquote(str_0)

if __name__ == "__main__":
    unittest.main()
