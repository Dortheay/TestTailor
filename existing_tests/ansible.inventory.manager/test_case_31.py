import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        str_0 = 'all'
        str_1 = '!exclude'
        str_2 = '&intersection'
        str_3 = 'host1'
        str_4 = '!another_exclude'
        str_5 = [str_0, str_1, str_2, str_3, str_4]
        var_0 = module_0.order_patterns(str_5)
        str_6 = '!exclude1'
        str_7 = '!exclude2'
        str_8 = [str_6, str_7]
        var_1 = module_0.order_patterns(str_8)
        str_9 = '&intersection1'
        str_10 = '&intersection2'
        str_11 = [str_9, str_10]
        var_2 = module_0.order_patterns(str_11)
        str_12 = [str_1, str_2]
        var_3 = module_0.order_patterns(str_12)
        var_4 = []
        var_5 = module_0.order_patterns(var_4)
        var_6 = None
        str_13 = ''
        var_7 = [str_0, var_6, str_13, str_1]
        var_8 = module_0.order_patterns(var_7)
        str_14 = 'host2'
        str_15 = [str_3, str_0, str_14]
        var_9 = module_0.order_patterns(str_15)

if __name__ == "__main__":
    unittest.main()
