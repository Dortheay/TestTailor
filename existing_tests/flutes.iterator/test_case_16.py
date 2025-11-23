import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '\tLI8_k&#]'
            float_0 = 0.0
            list_0 = [float_0, str_0, float_0, str_0]
            bool_0 = True
            int_0 = -3860
            map_list_0 = module_0.MapList(bool_0, int_0)
            range_0 = module_0.Range(*list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
