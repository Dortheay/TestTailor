import unittest
import timeout_decorator
import ansible.module_utils.common.sys_info as module_0

class Test_Sys_info_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\xfbqr\xe5\xbd\xd1|V\x82\xac"\x1bT\xf8\x17\x9a'
            var_0 = module_0.get_platform_subclass(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
