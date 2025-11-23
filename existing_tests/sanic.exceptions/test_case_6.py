import unittest
import timeout_decorator
import sanic.exceptions as module_0

class Test_Exceptions_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        float_0 = 980.9
        sanic_exception_0 = module_0.SanicException(float_0)
        int_0 = -495
        service_unavailable_0 = module_0.ServiceUnavailable(int_0)
        forbidden_0 = module_0.Forbidden(service_unavailable_0)
        set_0 = set()
        str_0 = 't}[uB'
        str_1 = 'Wq\x0br18BrR'
        str_2 = '.'
        header_not_found_0 = module_0.HeaderNotFound(str_1, str_2, set_0)
        dict_0 = {forbidden_0: str_0, header_not_found_0: str_1, float_0: float_0}
        str_3 = 'filename'
        str_4 = '`p:hA0w76t)_w^v-'
        str_5 = ' '
        dict_1 = {str_3: str_2, str_1: str_4, str_5: forbidden_0}
        not_found_0 = module_0.NotFound(dict_1)
        not_found_1 = module_0.NotFound(dict_0, not_found_0)
        not_found_2 = module_0.NotFound(str_0, not_found_1)
        not_found_3 = module_0.NotFound(set_0, not_found_2)
        u_r_l_build_error_0 = module_0.URLBuildError(not_found_3)
        tuple_0 = (sanic_exception_0,)
        bool_0 = False
        str_6 = 'l^+[?jAkx'
        str_7 = 'protocol.connection_lost'
        str_8 = ']Ju#y>7n\n/WO[v6;Q'
        dict_2 = {str_6: tuple_0, str_6: tuple_0, str_7: float_0, str_8: str_8}
        unauthorized_0 = module_0.Unauthorized(bool_0, **dict_2)
        service_unavailable_1 = module_0.ServiceUnavailable(tuple_0, unauthorized_0)
        invalid_signal_0 = module_0.InvalidSignal(service_unavailable_1)

if __name__ == "__main__":
    unittest.main()
