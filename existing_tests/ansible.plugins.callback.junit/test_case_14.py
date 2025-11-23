import unittest
import timeout_decorator
import ansible.plugins.callback.junit as module_0

class Test_Junit_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            list_0 = []
            bytes_0 = b'\x07U\xf96\xdb\xeb\xc2'
            set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
            tuple_0 = (set_0,)
            str_0 = '`'
            float_0 = 0.0001
            str_1 = ':&M},e\x0bT=\ric'
            host_data_0 = module_0.HostData(tuple_0, str_0, float_0, str_1)
            bytes_1 = b'n\xfa\x08/\xe7=\x02\x0c'
            task_data_0 = module_0.TaskData(bytes_0, host_data_0, set_0, bytes_1, set_0)
            var_0 = task_data_0.add_host(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
