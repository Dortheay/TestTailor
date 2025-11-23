import unittest
import timeout_decorator
import ansible.plugins.action.yum as module_0

class Test_Yum_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'BS\x0bM !)[5#1:ZMU-(3)N'
            list_0 = []
            list_1 = [str_0, str_0, list_0, str_0]
            str_1 = 'Gg*sI R'
            set_0 = {str_1}
            bytes_0 = b'\x00\xe9\x11g\xe5{h\xb8\x81"iA\xe8p\np\xedMY'
            str_2 = 'Dj'
            action_module_0 = module_0.ActionModule(set_0, list_1, list_0, bytes_0, str_2, list_1)
            action_module_1 = module_0.ActionModule(str_0, list_1, str_1, action_module_0, set_0, list_0)
            var_0 = action_module_1.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
