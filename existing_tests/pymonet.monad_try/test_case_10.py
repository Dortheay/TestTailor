import unittest
import timeout_decorator
import pymonet.monad_try as module_0

class Test_Monad_try_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        int_0 = None
        str_0 = '\n        Call success_callback function with monad value when monad is successfully.\n\n        :params success_callback: function to apply with monad value.\n        :type success_callback: Function(A)\n        :returns: self\n        :rtype: Try[A]\n        '
        bool_0 = False
        try_0 = module_0.Try(bool_0, bool_0)
        var_0 = try_0.get()
        dict_0 = {str_0: int_0}
        bool_1 = False
        try_1 = module_0.Try(dict_0, bool_1)
        str_1 = try_1.__str__()
        bool_2 = True
        bool_3 = True
        try_2 = module_0.Try(bool_2, bool_3)
        var_1 = try_2.get_or_else(str_0)
        bool_4 = None
        try_3 = module_0.Try(int_0, bool_4)
        str_2 = '\n    Function for return function depended on first function argument\n    cond get list of two-item tuples,\n    first is condition_function, second is execute_function.\n    Returns this execute_function witch first condition_function return truly value.\n\n    :param condition_list: list of two-item tuples (condition_function, execute_function)\n    :type condition_list: List[(Function, Function)]\n    :returns: Returns this execute_function witch first condition_function return truly value\n    :rtype: Function\n    '
        var_2 = try_3.get_or_else(try_2)
        var_3 = try_3.get()
        bool_5 = True
        try_4 = module_0.Try(str_2, bool_5)
        bool_6 = try_4.__eq__(try_3)

if __name__ == "__main__":
    unittest.main()
