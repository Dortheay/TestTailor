import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            set_0 = None
            var_0 = module_0.no_map_instance(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
