import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        list_0 = None
        var_0 = module_0.snake_dict_to_camel_dict(list_0)

if __name__ == "__main__":
    unittest.main()
