import unittest
import timeout_decorator
import ansible.utils.color as module_0

class Test_Color_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'Z\\\ryLvGU\x0bM]IqQ)0'
        bool_0 = False
        list_0 = [str_0, str_0, bool_0]
        var_0 = module_0.hostcolor(str_0, list_0)

if __name__ == "__main__":
    unittest.main()
