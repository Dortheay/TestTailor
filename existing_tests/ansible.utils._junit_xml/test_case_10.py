import unittest
import timeout_decorator
import ansible.utils._junit_xml as module_0

class Test__junit_xml_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        test_suites_0 = module_0.TestSuites()
        str_0 = test_suites_0.to_pretty_xml()

if __name__ == "__main__":
    unittest.main()
