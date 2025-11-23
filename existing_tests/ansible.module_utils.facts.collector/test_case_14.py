import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0
import collections as module_1

class Test_Collector_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            bytes_0 = b"\xa8\x899\x8b\xdd\xe6\xfa'\xe6"
            set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
            var_0 = module_0.resolve_requires(bytes_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
