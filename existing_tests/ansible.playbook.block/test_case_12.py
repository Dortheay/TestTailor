import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        bool_0 = False
        str_0 = '\x0b#<Yc'
        block_0 = module_0.Block(str_0)
        var_0 = block_0.filter_tagged_tasks(bool_0)

if __name__ == "__main__":
    unittest.main()
