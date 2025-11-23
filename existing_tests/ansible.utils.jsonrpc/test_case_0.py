import unittest
import timeout_decorator
import ansible.utils.jsonrpc as module_0

class Test_Jsonrpc_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        json_rpc_server_0 = module_0.JsonRpcServer()

if __name__ == "__main__":
    unittest.main()
