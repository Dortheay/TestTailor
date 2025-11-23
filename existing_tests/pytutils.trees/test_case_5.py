import unittest
import timeout_decorator
import pytutils.trees as module_0

class Test_Trees_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = ''
            str_1 = '7JuKe\x0c:T\x0b'
            str_2 = ''
            var_0 = module_0.set_tree_node(str_0, str_1, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
