import unittest
import timeout_decorator
import ansible.utils._junit_xml as module_0

class Test__junit_xml_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'F/ZV,Givhl]'
            test_failure_0 = module_0.TestFailure(str_0)
            str_1 = '(d'
            test_suite_0 = module_0.TestSuite(str_1, str_1)
            var_0 = test_suite_0.__eq__(test_failure_0)
            test_suite_1 = module_0.TestSuite(str_0, str_0, str_0)
            element_0 = test_suite_1.get_xml_element()
            list_0 = [test_suite_1, test_suite_0, test_suite_0, test_suite_1]
            test_suites_0 = module_0.TestSuites(str_1, list_0)
            str_2 = test_suites_0.to_pretty_xml()
            str_3 = 'CnlQ"'
            test_case_0 = module_0.TestCase(str_3, str_3)
            test_error_0 = module_0.TestError()
            var_1 = test_error_0.__repr__()
            var_2 = test_case_0.__repr__()
            var_3 = test_case_0.__repr__()
            test_error_1 = module_0.TestError()
            var_4 = test_error_0.__repr__()
            element_1 = test_case_0.get_xml_element()
            var_5 = test_error_1.__eq__(element_1)
            test_suites_1 = module_0.TestSuites()
            test_suite_2 = module_0.TestSuite(str_3)
            element_2 = test_suite_2.get_xml_element()
            test_suites_2 = module_0.TestSuites()
            str_4 = '$b!W|Cd3)FMwB\tXq%'
            list_1 = [test_suite_2, test_suite_2, test_suite_2]
            test_suites_3 = module_0.TestSuites(list_1)
            test_suite_3 = module_0.TestSuite(str_3, str_4, str_3)
            var_6 = test_suite_3.__repr__()
            element_3 = test_suites_2.get_xml_element()
            var_7 = test_error_1.__repr__()
            var_8 = test_suite_1.__repr__()
            set_0 = set()
            var_9 = test_error_1.__eq__(set_0)
            dict_0 = test_case_0.get_attributes()
            test_result_0 = module_0.TestResult()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
