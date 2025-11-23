import unittest
import timeout_decorator
import ansible.parsing.dataloader as module_0

class Test_Dataloader_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            float_0 = 658.542387
            data_loader_0 = module_0.DataLoader()
            str_0 = 'kn\\)hJE!'
            list_0 = [str_0, str_0, float_0, data_loader_0]
            float_1 = None
            bool_0 = True
            tuple_0 = (float_1, bool_0)
            str_1 = '~;P$-g~:S<@'
            set_0 = None
            var_0 = data_loader_0.path_dwim_relative_stack(list_0, tuple_0, str_1, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
