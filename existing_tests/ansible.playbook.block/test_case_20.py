import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        bytes_0 = b'}\xe3\x1eG\x96\x9c\xbfT\x0bf\x14&&'
        bool_0 = False
        bool_1 = True
        block_0 = module_0.Block(bool_0, bool_1)
        var_0 = block_0.filter_tagged_tasks(bytes_0)

if __name__ == "__main__":
    unittest.main()
