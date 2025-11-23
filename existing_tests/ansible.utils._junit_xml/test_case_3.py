import unittest
import timeout_decorator
import ansible.utils._junit_xml as module_0

class Test__junit_xml_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'wLXFbYG)c9'
            test_error_0 = module_0.TestError(str_0, str_0, str_0)
            test_suites_0 = module_0.TestSuites()
            str_1 = test_suites_0.to_pretty_xml()
            str_2 = 'rUDoM)'
            test_case_0 = module_0.TestCase(str_2)
            test_case_1 = module_0.TestCase(str_0, test_case_0, str_2, str_0, str_0, str_2, str_0)
            var_0 = test_error_0.__eq__(test_case_1)
            list_0 = [test_error_0, test_error_0]
            bool_0 = True
            test_case_2 = module_0.TestCase(str_0, str_0, list_0, bool_0)
            element_0 = test_case_2.get_xml_element()
            str_3 = 'rl|KT X 44RY'
            test_error_1 = module_0.TestError(str_3, str_3)
            str_4 = 'g'
            var_1 = test_case_2.__repr__()
            test_error_2 = module_0.TestError(str_4)
            test_result_0 = module_0.TestResult(test_error_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
