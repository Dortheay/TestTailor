import unittest
import timeout_decorator
import ansible.module_utils.connection as module_0

class Test_Connection_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'o=\tqyR?ct]X/#f2Hx'
        list_0 = [str_0]
        var_0 = module_0.request_builder(list_0)

if __name__ == "__main__":
    unittest.main()
