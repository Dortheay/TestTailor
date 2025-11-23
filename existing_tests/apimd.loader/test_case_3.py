import unittest
import timeout_decorator
import apimd.loader as module_0

class Test_Loader_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'O>y,u5}jl'
        iterator_0 = module_0.walk_packages(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
