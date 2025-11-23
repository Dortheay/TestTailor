import unittest
import timeout_decorator
import ansible.module_utils.facts.other.ohai as module_0

class Test_Ohai_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = -3919.3923
            ohai_fact_collector_0 = module_0.OhaiFactCollector()
            var_0 = ohai_fact_collector_0.get_ohai_output(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
