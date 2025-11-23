import unittest
import timeout_decorator
import ansible.modules.iptables as module_0

class Test_Iptables_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            float_0 = 1.0
            str_0 = 'Function to create a deep copy of module response data\n\n    Designed to be used within the Ansible "engine" to improve performance\n    issues where ``copy.deepcopy`` was used previously, largely with CPU\n    and memory contention.\n\n    This only supports the following data types, and was designed to only\n    handle specific workloads:\n\n    * ``dict``\n    * ``list``\n\n    The data we pass here will come from a serialization such\n    as JSON, so we shouldn\'t have need for other data types such as\n    ``set`` or ``tuple``.\n\n    Take note that this function should not be used extensively as a\n    replacement for ``deepcopy`` due to the naive way in which this\n    handles other data types.\n\n    Do not expect uses outside of those listed below to maintain\n    backwards compatibility, in case we need to extend this function\n    to handle our specific needs:\n\n    * ``ansible.executor.task_result.TaskResult.clean_copy``\n    * ``ansible.vars.clean.clean_facts``\n    * ``ansible.vars.namespace_facts``\n    '
            str_1 = '&.q9<n|PkS/9`eUCqd'
            tuple_0 = (float_0, str_0, str_1)
            bool_0 = False
            set_0 = {float_0, tuple_0, str_0, float_0}
            var_0 = module_0.get_chain_policy(tuple_0, bool_0, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
