import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        group_0 = module_0.Group()
        dict_0 = {}
        var_0 = group_0.deserialize(dict_0)
        str_0 = ';L[+V\n\t@'
        list_0 = [var_0]
        var_1 = group_0.set_variable(str_0, list_0)
        var_2 = group_0.__str__()
        var_3 = group_0.get_descendants()

if __name__ == "__main__":
    unittest.main()
