import unittest
import timeout_decorator
import ansible.utils._junit_xml as module_0

class Test__junit_xml_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        test_suites_0 = module_0.TestSuites()

if __name__ == "__main__":
    unittest.main()
