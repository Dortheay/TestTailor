import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        get_with_context_result_0 = None
        float_0 = -3331.385
        var_0 = module_0.get_shell_plugin(get_with_context_result_0, float_0)

if __name__ == "__main__":
    unittest.main()
