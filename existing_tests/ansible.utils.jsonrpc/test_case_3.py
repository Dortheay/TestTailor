import unittest
import timeout_decorator
import ansible.utils.jsonrpc as module_0
import json as module_1

class Test_Jsonrpc_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            json_rpc_server_0 = module_0.JsonRpcServer()
            var_0 = json_rpc_server_0.invalid_request(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
