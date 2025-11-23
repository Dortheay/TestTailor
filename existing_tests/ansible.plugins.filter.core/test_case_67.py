import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_68(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        list_0 = []
        list_1 = [list_0, list_0, list_0, list_0]
        var_0 = module_0.flatten(list_1)

if __name__ == "__main__":
    unittest.main()
