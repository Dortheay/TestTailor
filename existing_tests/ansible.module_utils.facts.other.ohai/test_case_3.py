import unittest
import timeout_decorator
import ansible.module_utils.facts.other.ohai as module_0

class Test_Ohai_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            set_0 = None
            str_0 = '9K.PznA*hUyy0?yt'
            ohai_fact_collector_0 = module_0.OhaiFactCollector(set_0)
            var_0 = ohai_fact_collector_0.collect(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
