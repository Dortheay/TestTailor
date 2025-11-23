import unittest
import timeout_decorator
import ansible.modules.systemd as module_0

class Test_Systemd_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = '\'"+fR"RDr<U`=oS/'
        var_0 = module_0.parse_systemctl_show(str_0)
        var_1 = module_0.request_was_ignored(str_0)
        var_2 = module_0.main()
        str_1 = 'fE19-%AM-t?^{A'
        var_3 = module_0.request_was_ignored(str_1)
        str_2 = "J}s u+?\x0bg\rPG<\x0bT'"
        var_4 = module_0.is_deactivating_service(str_2)
        dict_0 = {}
        var_5 = module_0.is_deactivating_service(dict_0)
        var_6 = module_0.main()

if __name__ == "__main__":
    unittest.main()
