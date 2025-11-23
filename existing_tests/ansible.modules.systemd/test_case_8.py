import unittest
import timeout_decorator
import ansible.modules.systemd as module_0

class Test_Systemd_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'ActiveState=active'
        str_1 = 'ExecStart={ path=/usr/sbin/crond ; argv[]=/usr/sbin/crond -n $CRONDARGS ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }'
        str_2 = 'Description={ Single-line description starting with { character '
        str_3 = 'AnotherKey=another_value'
        str_4 = 'ExecReload={ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }'
        str_5 = [str_0, str_1, str_2, str_3, str_4]
        var_0 = module_0.parse_systemctl_show(str_5)

if __name__ == "__main__":
    unittest.main()
