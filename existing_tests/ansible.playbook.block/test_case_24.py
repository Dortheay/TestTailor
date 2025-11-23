import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'Iq^'
            list_0 = [str_0, str_0, str_0]
            float_0 = 0.001
            dict_0 = {float_0: float_0, float_0: float_0}
            str_1 = ''
            block_0 = module_0.Block(float_0, dict_0, str_1)
            var_0 = block_0.__eq__(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
