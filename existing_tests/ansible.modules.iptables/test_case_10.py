import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\xde\x1fLn\xc0\x04\xb8`\x11\xbd+\x85\xab[\x8a5wf\x08T'
            float_0 = None
            str_0 = 's$OO%IHMfTw1@'
            list_0 = [str_0]
            var_0 = module_0.append_param(bytes_0, float_0, list_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
