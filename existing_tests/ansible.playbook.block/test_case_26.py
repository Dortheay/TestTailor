import unittest
import timeout_decorator
import ansible.playbook.block as module_0

class Test_Block_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            tuple_0 = ()
            bytes_0 = b'\x93\x9e\xbc\x00\xa6\xf5&\xc4AW'
            tuple_1 = (bytes_0,)
            block_0 = module_0.Block(tuple_1, tuple_1, bytes_0)
            var_0 = block_0.filter_tagged_tasks(tuple_0)
            str_0 = 'xB^#UF}qm)pA13'
            block_1 = module_0.Block(str_0, str_0)
            var_1 = block_1.get_vars()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
