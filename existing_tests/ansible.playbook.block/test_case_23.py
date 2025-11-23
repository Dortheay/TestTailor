import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = False
            bool_0 = True
            block_0 = module_0.Block(int_0, bool_0)
            var_0 = block_0.copy()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
