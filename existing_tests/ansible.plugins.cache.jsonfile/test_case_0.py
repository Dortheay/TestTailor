import unittest
import timeout_decorator
import ansible.plugins.cache.jsonfile as module_0

class Test_Jsonfile_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            cache_module_0 = module_0.CacheModule()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
