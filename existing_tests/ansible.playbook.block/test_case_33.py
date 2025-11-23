import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            block_0 = module_0.Block()
            var_0 = block_0.get_dep_chain()
            int_0 = -1219
            str_0 = '\tb[\t'
            str_1 = ';7*_'
            block_1 = module_0.Block(int_0, str_0, str_1)
            var_1 = block_1.get_first_parent_include()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
