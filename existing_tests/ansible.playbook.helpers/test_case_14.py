import unittest
import timeout_decorator
import ansible.playbook.helpers as module_0

class Test_Helpers_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'test3'
        str_1 = 'mocked_play'
        int_0 = None
        dict_0 = {str_1: str_0}
        bytes_0 = None
        float_0 = None
        set_0 = {int_0}
        var_0 = module_0.load_list_of_blocks(int_0, dict_0, bytes_0, int_0, float_0, set_0)
        var_1 = None
        list_0 = [var_1]
        str_2 = 'SJ\ncjysp\x0cq'
        tuple_0 = (list_0, list_0)
        var_2 = module_0.load_list_of_blocks(list_0, int_0, str_2, tuple_0)

if __name__ == "__main__":
    unittest.main()
