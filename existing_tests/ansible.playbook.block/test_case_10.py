import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        str_0 = 'dep_chain'
        str_1 = 'role'
        str_2 = 'parent'
        str_3 = 'parent_type'
        str_4 = 'dependency1'
        str_5 = 'dependency2'
        str_6 = [str_4, str_5]
        str_7 = 'name'
        str_8 = 'mock_role'
        str_9 = {str_7: str_8}
        str_10 = 'mock_parent'
        str_11 = {str_7: str_10}
        str_12 = 'Block'
        str_13 = {str_0: str_6, str_1: str_9, str_2: str_11, str_3: str_12}
        block_0 = module_0.Block()
        var_0 = block_0.deserialize(str_13)

if __name__ == "__main__":
    unittest.main()
