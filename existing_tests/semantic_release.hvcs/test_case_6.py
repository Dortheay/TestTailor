import unittest
import timeout_decorator
import semantic_release.hvcs as module_0

class Test_Hvcs_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = 'kg_~P\tf0~Xl?UQ'
        optional_0 = module_0.get_token()
        str_1 = '9bI:K'
        str_2 = None
        base_0 = module_0.get_hvcs()
        bool_0 = base_0.check_build_status(str_0, str_1, str_2)
        optional_1 = base_0.token()
        base_1 = module_0.Base()
        base_2 = module_0.get_hvcs()
        gitlab_0 = module_0.Gitlab()
        optional_2 = base_2.token()
        optional_3 = module_0.get_domain()
        token_auth_0 = module_0.TokenAuth(gitlab_0)
        str_3 = '$T}g2u\r'
        set_0 = {gitlab_0, gitlab_0}
        optional_4 = gitlab_0.token()
        var_0 = token_auth_0.__eq__(set_0)
        bool_1 = module_0.upload_to_release(str_0, str_0, str_3, str_0)

if __name__ == "__main__":
    unittest.main()
