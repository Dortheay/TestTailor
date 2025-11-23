import unittest
import timeout_decorator
import sanic.mixins.routes as module_0

class Test_Routes_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'Writes a chunk of data to the streaming response.\n\n        :param data: str or bytes-ish data to be written.\n        '
        bool_0 = False
        str_1 = 'c$!;}\\aX_woG'
        dict_0 = {str_1: str_1, str_1: str_1}
        route_mixin_0 = module_0.RouteMixin(**dict_0)
        var_0 = route_mixin_0.put(str_0, bool_0, str_0)

if __name__ == "__main__":
    unittest.main()
