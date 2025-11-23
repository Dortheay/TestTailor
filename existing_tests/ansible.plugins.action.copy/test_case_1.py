import unittest
import timeout_decorator
import ansible.plugins.action.copy as module_0

class Test_Copy_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = ''
            int_0 = -2780
            str_1 = 'lkWWa|"v5.-.'
            str_2 = '5$y\x0b`9m\\{'
            set_0 = {str_1, str_2}
            bool_0 = False
            bytes_0 = b''
            str_3 = 'B!Kq#D`Xv'
            action_module_0 = module_0.ActionModule(str_1, set_0, bool_0, set_0, bytes_0, str_3)
            var_0 = action_module_0.run(str_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
