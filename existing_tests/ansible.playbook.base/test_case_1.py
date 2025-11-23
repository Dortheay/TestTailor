import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        base_0 = module_0.Base()
        var_0 = base_0.get_search_path()

if __name__ == "__main__":
    unittest.main()
