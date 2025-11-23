import unittest
import timeout_decorator
import flutes.structure as module_0

class Test_Structure_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'BmJojb"Kn>\t4'
            tuple_0 = ()
            var_0 = module_0.map_structure(str_0, tuple_0)
            bytes_0 = b'`\x15\x92\x8bM\xcd\xcf&\x8a'
            float_0 = None
            var_1 = module_0.map_structure(bytes_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
