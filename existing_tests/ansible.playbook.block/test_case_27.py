import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'oI}V$m'
            bool_0 = None
            bytes_0 = b'x\x06'
            block_0 = module_0.Block(bytes_0)
            var_0 = block_0.load(str_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
