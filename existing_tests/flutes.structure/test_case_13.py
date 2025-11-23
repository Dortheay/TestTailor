import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = 'jL4Ft)*'
            dict_0 = {}
            var_0 = module_0.map_structure_zip(dict_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
