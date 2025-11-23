import unittest
import timeout_decorator
import ansible.vars.manager as module_0

class Test_Manager_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            vars_with_sources_0 = module_0.VarsWithSources()
            var_0 = vars_with_sources_0.__iter__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
