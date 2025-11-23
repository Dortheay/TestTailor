import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        float_0 = 0.2
        list_0 = [float_0, float_0, float_0, float_0]
        var_0 = module_0.jsonify(list_0)

if __name__ == "__main__":
    unittest.main()
