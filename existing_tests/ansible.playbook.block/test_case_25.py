import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = ':f}AW|n|;F'
            bool_0 = None
            set_0 = None
            tuple_0 = (str_0, bool_0, set_0)
            set_1 = {tuple_0, bool_0}
            int_0 = -1495
            block_0 = module_0.Block(int_0)
            var_0 = block_0.__ne__(set_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
