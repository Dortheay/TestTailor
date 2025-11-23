import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        set_0 = None
        var_0 = module_0.jsonify(set_0)

if __name__ == "__main__":
    unittest.main()
