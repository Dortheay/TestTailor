import unittest
import timeout_decorator
import mimesis.builtins.en as module_0
import builtins as module_1

class Test_En_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        list_0 = []
        bytearray_0 = module_1.bytearray(*list_0)
        u_s_a_spec_provider_0 = module_0.USASpecProvider(bytearray_0)
        str_0 = u_s_a_spec_provider_0.tracking_number()

if __name__ == "__main__":
    unittest.main()
