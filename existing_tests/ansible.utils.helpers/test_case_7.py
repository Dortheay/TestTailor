import unittest
import timeout_decorator
import ansible.utils.helpers as module_0

class Test_Helpers_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'TF8L>`'
        var_0 = module_0.deduplicate_list(str_0)

if __name__ == "__main__":
    unittest.main()
