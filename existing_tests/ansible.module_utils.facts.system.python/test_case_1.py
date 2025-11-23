import unittest
import timeout_decorator
import ansible.module_utils.facts.system.python as module_0

class Test_Python_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        python_fact_collector_0 = module_0.PythonFactCollector()
        var_0 = python_fact_collector_0.collect()

if __name__ == "__main__":
    unittest.main()
