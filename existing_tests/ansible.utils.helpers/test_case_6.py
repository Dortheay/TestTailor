import unittest
import timeout_decorator
import ansible.utils.helpers as module_0

class Test_Helpers_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'i12BwpBv,{FM'
        tuple_0 = (str_0,)
        bool_0 = True
        var_0 = module_0.object_to_dict(tuple_0, bool_0)

if __name__ == "__main__":
    unittest.main()
