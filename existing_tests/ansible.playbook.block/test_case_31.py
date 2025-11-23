import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            int_0 = -2794
            int_1 = 1211
            bytes_0 = b'RF\xa3\t\x84\xd5hi\x8e\xa3\xb9\xb7\x14\xab\xd4'
            set_0 = {int_1, bytes_0}
            block_0 = module_0.Block(int_1, set_0)
            var_0 = block_0.deserialize(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
