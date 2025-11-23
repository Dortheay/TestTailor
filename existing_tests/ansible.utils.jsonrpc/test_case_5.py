import unittest
import timeout_decorator
import ansible.utils.jsonrpc as module_0
import json as module_1

class Test_Jsonrpc_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            json_rpc_server_0 = module_0.JsonRpcServer()
            var_0 = json_rpc_server_0.parse_error()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
