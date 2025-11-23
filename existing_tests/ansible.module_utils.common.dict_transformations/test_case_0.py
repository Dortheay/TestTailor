import unittest
import timeout_decorator
import ansible.module_utils.common.dict_transformations as module_0

class Test_Dict_transformations_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'G?sq5S3}v\r'
            var_0 = module_0.camel_dict_to_snake_dict(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
