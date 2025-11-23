import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        block_0 = module_0.Block()
        str_0 = 'block'
        str_1 = 'key'
        str_2 = 'value'
        str_3 = {str_1: str_2}
        str_4 = [str_3]
        var_0 = block_0.preprocess_data(str_4)
        str_5 = {str_1: str_2}
        var_1 = block_0.preprocess_data(str_5)
        str_6 = {str_1: str_2}
        str_7 = [str_6]
        str_8 = {str_0: str_7}
        var_2 = block_0.preprocess_data(str_8)

if __name__ == "__main__":
    unittest.main()
