import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_config as module_0

class Test__collection_config_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        event_source_0 = module_0._EventSource()

if __name__ == "__main__":
    unittest.main()
