import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            float_0 = 100.0
            var_0 = module_0.dict_to_list_of_dict_key_value_elements(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
