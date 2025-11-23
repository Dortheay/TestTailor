import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            int_0 = False
            str_0 = 'v'
            int_1 = -1189
            list_0 = [int_0, int_0, int_1]
            block_0 = module_0.Block(int_1, list_0)
            var_0 = block_0.deserialize(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
