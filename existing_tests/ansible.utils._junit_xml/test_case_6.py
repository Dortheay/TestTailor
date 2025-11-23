import unittest
import timeout_decorator
import ansible.utils._junit_xml as module_0

class Test__junit_xml_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = '=\x0cS>OP=`wN:'
        test_failure_0 = module_0.TestFailure(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
