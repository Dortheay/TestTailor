import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_37(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        try:
            set_0 = set()
            bytes_0 = b'\x1b\x1a p\x10\xa9'
            block_0 = module_0.Block(set_0, bytes_0)
            var_0 = block_0.all_parents_static()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
