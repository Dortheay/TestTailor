import unittest
import timeout_decorator
import ansible.plugins.action.assemble as module_0

class Test_Assemble_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = -1219.03
            bytes_0 = b'T\xd8\x19\xc7\xce\x1a;8\x15\x9b\xdc,\x13{lG\xd7.'
            bytes_1 = b'`\xa1\xb8R\xccl%"^\xb09\xa95\x96\xc29\x1e'
            dict_0 = {float_0: float_0, bytes_1: float_0, bytes_1: float_0}
            list_0 = [dict_0, dict_0]
            tuple_0 = (list_0, dict_0)
            set_0 = {float_0}
            action_module_0 = module_0.ActionModule(float_0, bytes_0, bytes_1, dict_0, tuple_0, set_0)
            var_0 = action_module_0.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
