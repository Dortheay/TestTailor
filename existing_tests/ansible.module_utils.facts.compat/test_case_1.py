import unittest
import timeout_decorator
import ansible.module_utils.facts.compat as module_0

class Test_Compat_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            list_0 = None
            var_0 = module_0.get_all_facts(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
