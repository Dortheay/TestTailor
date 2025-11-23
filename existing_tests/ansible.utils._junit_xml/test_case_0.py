import unittest
import timeout_decorator
import ansible.utils._junit_xml as module_0

class Test__junit_xml_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = "M'V@0KTt\x0b\x0cgf{|2\t )="
            str_1 = 'Failed creating tmp file for atomic move.  This usually happens when using Python3 less than Python3.5. Please use Python2.x or Python3.5 or greater.'
            str_2 = None
            str_3 = 'uaYRd@ncc='
            str_4 = 'Unable to parse %s as an inventory source'
            dict_0 = {str_1: str_2, str_3: str_0, str_3: str_3, str_4: str_0}
            test_failure_0 = module_0.TestFailure(str_1)
            list_0 = [test_failure_0, test_failure_0, test_failure_0]
            test_case_0 = module_0.TestCase(str_0, dict_0, str_4, str_3, list_0, str_1)
            element_0 = test_case_0.get_xml_element()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
