import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_config as module_0

class Test__collection_config_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            event_source_0 = module_0._EventSource()
            bytes_0 = b'\x10;\xca\x8a\xaaFD\xb9\x96%1\xfe\xff^\x96gX\xd1\x8fm'
            var_0 = event_source_0.__iadd__(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
