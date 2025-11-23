import unittest
import timeout_decorator
import ansible.plugins.callback.junit as module_0

class Test_Junit_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'task1'
        str_1 = 'Test Task'
        str_2 = '/path/to/task'
        str_3 = 'Play Name'
        str_4 = 'Test Action'
        task_data_0 = module_0.TaskData(str_0, str_1, str_2, str_3, str_4)
        str_5 = 'host1'
        str_6 = 'Host One'
        str_7 = 'ok'
        str_8 = 'Result 1'
        host_data_0 = module_0.HostData(str_5, str_6, str_7, str_8)
        str_9 = 'included'
        host_data_1 = module_0.HostData(str_5, str_6, str_9, str_8)
        var_0 = task_data_0.add_host(host_data_0)
        var_1 = task_data_0.host_data
        var_2 = len(var_1)
        var_3 = task_data_0.add_host(host_data_1)
        var_4 = task_data_0.host_data
        var_5 = len(var_4)

if __name__ == "__main__":
    unittest.main()
