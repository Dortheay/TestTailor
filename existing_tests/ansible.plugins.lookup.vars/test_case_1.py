import unittest
import timeout_decorator
import ansible.plugins.lookup.vars as module_0

class Test_Vars_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'The time to wait for the collection import process to finish.'
            tuple_0 = (str_0,)
            lookup_module_0 = module_0.LookupModule()
            var_0 = lookup_module_0.run(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
