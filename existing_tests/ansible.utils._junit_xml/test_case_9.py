import unittest
import timeout_decorator
import ansible.utils._junit_xml as module_0

class Test__junit_xml_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = ')m[r$\nJj\ni\x0cb4'
        test_suite_0 = module_0.TestSuite(str_0, str_0, str_0)
        element_0 = test_suite_0.get_xml_element()

if __name__ == "__main__":
    unittest.main()
