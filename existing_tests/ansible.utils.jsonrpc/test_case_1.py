import unittest
import timeout_decorator
import ansible.utils.jsonrpc as module_0
import json as module_1

class Test_Jsonrpc_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            json_rpc_server_0 = module_0.JsonRpcServer()
            str_0 = 'value'
            str_1 = {str_0: str_0}
            str_2 = 'jsonrpc'
            str_3 = 'method'
            str_4 = 'params'
            str_5 = 'id'
            str_6 = '2.0'
            str_7 = 'unknown_method'
            var_0 = []
            var_1 = [var_0, str_1]
            int_0 = 2
            var_2 = {str_2: str_6, str_3: str_7, str_4: var_1, str_5: int_0}
            var_3 = module_1.dumps(var_2)
            var_4 = json_rpc_server_0.handle_request(var_3)
            str_8 = '_private_method'
            json_rpc_server_1 = module_0.JsonRpcServer()
            var_5 = []
            var_6 = {}
            var_7 = [var_5, var_6]
            var_8 = {str_2: str_6, str_3: str_8, str_4: var_7, str_5: int_0}
            var_9 = module_1.dumps(var_8)
            var_10 = json_rpc_server_0.handle_request(var_9)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
