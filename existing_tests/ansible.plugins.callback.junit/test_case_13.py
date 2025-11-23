import unittest
import timeout_decorator
import ansible.plugins.callback.junit as module_0

class Test_Junit_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            bytes_0 = b'?\x1c\xf1d\xca3\x918\xbc]\xd4:Y\xe2\xc9\xfe\x8c=\xffS'
            callback_module_0 = module_0.CallbackModule()
            var_0 = callback_module_0.v2_playbook_on_include(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
