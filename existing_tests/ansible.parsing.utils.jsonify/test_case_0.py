import unittest
import timeout_decorator
import ansible.parsing.utils.jsonify as module_0

class Test_Jsonify_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\xce\x85\x13\xb5O\xe5#m#^y\xba+\x92*E\xcf\x85'
            var_0 = module_0.jsonify(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
