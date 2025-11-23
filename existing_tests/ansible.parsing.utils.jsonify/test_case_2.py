import unittest
import timeout_decorator
import ansible.parsing.utils.jsonify as module_0

class Test_Jsonify_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        float_0 = -3461.8621
        var_0 = module_0.jsonify(float_0)

if __name__ == "__main__":
    unittest.main()
