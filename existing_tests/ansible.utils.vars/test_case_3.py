import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        bytes_0 = None
        var_0 = module_0.load_options_vars(bytes_0)

if __name__ == "__main__":
    unittest.main()
