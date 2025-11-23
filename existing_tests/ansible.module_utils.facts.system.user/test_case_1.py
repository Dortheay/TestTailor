import unittest
import timeout_decorator
import ansible.module_utils.facts.system.user as module_0

class Test_User_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bytes_0 = b'\n\xc2\xe2\x1d\xba\n\xbd\xfa'
        user_fact_collector_0 = module_0.UserFactCollector()
        var_0 = user_fact_collector_0.collect(bytes_0)

if __name__ == "__main__":
    unittest.main()
