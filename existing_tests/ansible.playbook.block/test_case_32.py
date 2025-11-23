import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = 'T4APSFe}aU807K'
            bytes_0 = b'h\xda7@\xbb\xf9\xcf\xd0\xdc\x13\x14\x0f\xa1\xe6'
            bool_0 = True
            block_0 = module_0.Block(str_0, bytes_0, bool_0)
            var_0 = block_0.serialize()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
