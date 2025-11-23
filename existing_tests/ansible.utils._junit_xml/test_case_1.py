import unittest
import timeout_decorator
import ansible.utils._junit_xml as module_0

class Test__junit_xml_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'fA'
            test_suite_0 = module_0.TestSuite(str_0, str_0, str_0, str_0, str_0)
            element_0 = test_suite_0.get_xml_element()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
