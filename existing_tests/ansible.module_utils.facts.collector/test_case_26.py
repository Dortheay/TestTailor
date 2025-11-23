import unittest
import timeout_decorator
import ansible.module_utils.facts.collector as module_0

class Test_Collector_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'network'
        str_1 = 'hardware'
        str_2 = {str_0, str_1}
        str_3 = 'software'
        str_4 = 'NetworkCollector'
        str_5 = [str_4]
        str_6 = 'HardwareCollector'
        str_7 = [str_6]
        str_8 = 'SoftwareCollector'
        str_9 = [str_8]
        str_10 = {str_0: str_5, str_1: str_7, str_3: str_9}
        var_0 = module_0.select_collector_classes(str_2, str_10)
        var_1 = set(var_0)
        var_2 = set(str_7)

if __name__ == "__main__":
    unittest.main()
