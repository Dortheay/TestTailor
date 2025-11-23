import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        set_0 = None
        set_1 = {set_0, set_0, set_0, set_0}
        var_0 = module_0.jsonify(set_1)

if __name__ == "__main__":
    unittest.main()
