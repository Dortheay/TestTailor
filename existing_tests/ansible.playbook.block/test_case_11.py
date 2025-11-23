import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        block_0 = module_0.Block()
        var_0 = block_0.filter_tagged_tasks(block_0)
        bytes_0 = b'\x18gv\xae\xa3\xd2\xd3E\xcd3\x8b\x17m*\xb9\xb3g<\xef\x14'
        var_1 = block_0.set_loader(bytes_0)

if __name__ == "__main__":
    unittest.main()
