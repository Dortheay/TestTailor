import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'Z\r2dF{\nn\\#A}y/'
        list_0 = [str_0, str_0, str_0, str_0]
        var_0 = module_0.order_patterns(list_0)

if __name__ == "__main__":
    unittest.main()
