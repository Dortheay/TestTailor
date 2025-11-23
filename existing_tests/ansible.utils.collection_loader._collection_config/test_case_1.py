import unittest
import timeout_decorator
import ansible.utils.collection_loader._collection_config as module_0

class Test__collection_config_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'User instantiated - platform %s'
            event_source_0 = module_0._EventSource()
            var_0 = event_source_0.fire()
            set_0 = None
            var_1 = event_source_0.__isub__(set_0)
            float_0 = 1923.5
            str_1 = '\\\\(\\d+)'
            ansible_collection_config_0 = module_0.AnsibleCollectionConfig()
            dict_0 = {str_0: float_0, str_1: str_0, str_0: float_0}
            event_source_1 = module_0._EventSource()
            var_2 = event_source_1.__isub__(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
