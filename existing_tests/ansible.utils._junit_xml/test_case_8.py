import unittest
import timeout_decorator
import ansible.utils._junit_xml as module_0

class Test__junit_xml_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'protocol'
        test_case_0 = module_0.TestCase(str_0, str_0, str_0, str_0)
        element_0 = test_case_0.get_xml_element()
        test_suites_0 = module_0.TestSuites()
        str_1 = test_suites_0.to_pretty_xml()

if __name__ == "__main__":
    unittest.main()
