import unittest
import timeout_decorator
import ansible.utils.jsonrpc as module_0
import json as module_1

class Test_Jsonrpc_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            json_rpc_server_0 = module_0.JsonRpcServer()
            str_0 = 'jsonrpc'
            str_1 = 'method'
            str_2 = 'params'
            str_3 = 'some_method'
            var_0 = []
            var_1 = {}
            var_2 = [var_0, var_1]
            int_0 = 1
            var_3 = {str_0: str_0, str_1: str_3, str_2: var_2, str_0: int_0}
            var_4 = module_1.dumps(var_3)
            str_4 = 'rpc.invalid_method'
            var_5 = {str_0: str_0, str_1: str_4, str_2: int_0, str_0: int_0}
            var_6 = module_1.dumps(var_5)
            str_5 = 'nonexistent_method'
            bool_0 = None
            var_7 = json_rpc_server_0.register(bool_0)
            var_8 = {str_0: str_3, str_1: str_5, str_2: var_2, str_1: int_0}
            var_9 = module_1.dumps(var_8)
            var_10 = json_rpc_server_0.handle_request(var_4)
            var_11 = module_1.loads(var_10)
            var_12 = json_rpc_server_0.handle_request(var_6)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
