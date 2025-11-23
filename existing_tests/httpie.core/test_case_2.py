import unittest
import timeout_decorator
import httpie.core as module_0
import httpie.context as module_1

class Test_Core_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        environment_0 = module_1.Environment()
        var_0 = module_0.print_debug_info(environment_0)

if __name__ == "__main__":
    unittest.main()
