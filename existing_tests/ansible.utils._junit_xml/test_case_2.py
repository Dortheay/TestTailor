import unittest
import timeout_decorator
import ansible.utils._junit_xml as module_0

class Test__junit_xml_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            test_suites_0 = module_0.TestSuites()
            str_0 = 'cwM9ecG'
            bool_0 = True
            test_failure_0 = module_0.TestFailure()
            var_0 = test_failure_0.__repr__()
            test_case_0 = module_0.TestCase(str_0, bool_0)
            dict_0 = test_case_0.get_attributes()
            element_0 = test_case_0.get_xml_element()
            element_1 = test_case_0.get_xml_element()
            test_failure_1 = module_0.TestFailure()
            str_1 = '^k(%$R4\t#8oaYe"zJk'
            test_error_0 = module_0.TestError(str_1, str_1)
            list_0 = [test_case_0, test_case_0, test_case_0, test_case_0]
            element_2 = test_case_0.get_xml_element()
            test_suite_0 = module_0.TestSuite(str_0, str_0, list_0)
            list_1 = [test_suite_0]
            test_suites_1 = module_0.TestSuites(str_0, list_1)
            dict_1 = test_suites_1.get_attributes()
            dict_2 = test_suite_0.get_attributes()
            test_result_0 = module_0.TestResult(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
