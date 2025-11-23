import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            int_0 = 571
            float_0 = 1682.98
            bool_0 = False
            tuple_0 = (int_0,)
            block_0 = module_0.Block(float_0, bool_0, tuple_0)
            var_0 = block_0.serialize()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
