import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bytes_0 = b'7zj\xf9\xf5\xc7Tp'
            str_0 = 'P16\t$s?ofRhRv"'
            list_0 = [bytes_0, bytes_0, str_0]
            str_1 = '4vRKc$7}Og6i>5'
            dict_0 = {}
            str_2 = "Don't wait for import results."
            block_0 = module_0.Block(str_2)
            var_0 = block_0.load(list_0, str_1, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
