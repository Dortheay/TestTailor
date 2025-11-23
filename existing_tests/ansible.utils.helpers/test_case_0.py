import unittest
import timeout_decorator
import ansible.utils.helpers as module_0

class Test_Helpers_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            tuple_0 = None
            var_0 = module_0.deduplicate_list(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
