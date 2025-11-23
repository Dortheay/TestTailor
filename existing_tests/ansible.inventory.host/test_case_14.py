import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        list_0 = None
        tuple_0 = None
        dict_0 = {list_0: list_0, list_0: list_0, tuple_0: tuple_0, list_0: tuple_0}
        host_0 = module_0.Host()
        var_0 = host_0.deserialize(dict_0)

if __name__ == "__main__":
    unittest.main()
