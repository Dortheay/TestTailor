import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        type_0 = None
        module_0.register_no_map_class(type_0)

if __name__ == "__main__":
    unittest.main()
