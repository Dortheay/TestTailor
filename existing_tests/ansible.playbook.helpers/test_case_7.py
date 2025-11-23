import unittest
import timeout_decorator
import ansible.playbook.helpers as module_0

class Test_Helpers_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            list_0 = []
            dict_0 = None
            int_0 = 3003
            str_0 = '1J\x0bnA/u>;Wuqe&y,1r;d'
            var_0 = module_0.load_list_of_tasks(list_0, dict_0, int_0, int_0, str_0)
            bytes_0 = b'v\\g\xdaT\x13\x15\xda\xca\xe7\xd2x\xf2\x90\x03E\x03\xe9\x84'
            bool_0 = None
            tuple_0 = (list_0, bool_0, dict_0)
            str_1 = 'L}ViT%\n0\r`,\r'
            set_0 = None
            str_2 = 'IIAEGNCY5'
            var_1 = module_0.load_list_of_blocks(tuple_0, str_1, set_0, str_2, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
