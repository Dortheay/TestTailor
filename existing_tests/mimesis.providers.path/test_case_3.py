import unittest
import timeout_decorator
import mimesis.providers.path as module_0

class Test_Path_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'linux'
        str_1 = 'win32'
        dict_0 = {}
        path_0 = module_0.Path(**dict_0)
        str_2 = path_0.home()
        path_1 = module_0.Path(str_0)
        var_0 = path_1._pathlib_home
        var_1 = path_1._pathlib_home
        var_2 = str(var_1)
        path_2 = module_0.Path(str_1)
        var_3 = path_2._pathlib_home
        var_4 = path_2._pathlib_home
        list_0 = []
        path_3 = module_0.Path(*list_0, **dict_0)
        str_3 = path_3.users_folder()
        var_5 = str(var_4)

if __name__ == "__main__":
    unittest.main()
