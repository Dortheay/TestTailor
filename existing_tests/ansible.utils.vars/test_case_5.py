import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        bytes_0 = b'\xa2'
        bool_0 = False
        tuple_0 = (bool_0,)
        var_0 = module_0._isidentifier_PY3(tuple_0)
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        var_1 = module_0.load_extra_vars(list_0)
        list_1 = None
        var_2 = module_0.load_extra_vars(list_1)

if __name__ == "__main__":
    unittest.main()
