import unittest
import timeout_decorator
import pytutils.env as module_0

class Test_Env_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'o9k=]XszM^"cx'
        list_0 = [str_0]
        mutable_mapping_0 = None
        ordered_dict_0 = module_0.load_env_file(list_0, mutable_mapping_0)
        str_1 = 'Oz'
        str_2 = module_0.expand(str_1)
        str_3 = module_0.expand(str_0)
        str_4 = 'monokai'
        str_5 = module_0.expand(str_4)

if __name__ == "__main__":
    unittest.main()
