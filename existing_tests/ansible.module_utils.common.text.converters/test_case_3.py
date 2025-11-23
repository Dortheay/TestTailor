import unittest
import timeout_decorator
import ansible.module_utils.common.text.converters as module_0

class Test_Converters_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            list_0 = []
            var_0 = module_0.container_to_bytes(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
