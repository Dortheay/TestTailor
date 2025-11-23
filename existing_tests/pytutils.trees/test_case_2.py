import unittest
import timeout_decorator
import pytutils.trees as module_0

class Test_Trees_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\x9e\xf9\xdc\xc6\xb8\x19'
            str_0 = ",=+F!7'/?z"
            var_0 = module_0.get_tree_node(bytes_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
