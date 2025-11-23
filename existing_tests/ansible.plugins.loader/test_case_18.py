import unittest
import timeout_decorator
import ansible.plugins.loader as module_0

class Test_Loader_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            int_0 = -657
            bool_0 = False
            bytes_0 = b'\x93\xc9?s_e.V\x12"'
            str_0 = 'E9YOe"$P\rE9Hu>'
            list_0 = [int_0, int_0, str_0]
            float_0 = 615.59291
            jinja2_loader_0 = module_0.Jinja2Loader(bool_0, bytes_0, str_0, list_0, float_0)
            var_0 = jinja2_loader_0.all()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
