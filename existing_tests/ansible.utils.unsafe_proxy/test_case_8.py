import unittest
import timeout_decorator
import ansible.utils.unsafe_proxy as module_0

class Test_Unsafe_proxy_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        ansible_unsafe_text_0 = module_0.AnsibleUnsafeText()

if __name__ == "__main__":
    unittest.main()
