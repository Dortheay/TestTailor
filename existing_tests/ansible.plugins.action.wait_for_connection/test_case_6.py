import unittest
import timeout_decorator
import ansible.plugins.action.wait_for_connection as module_0

class Test_Wait_for_connection_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        float_0 = -919.57579
        str_0 = None
        dict_0 = {str_0: str_0}
        list_0 = [dict_0, float_0]
        timed_out_exception_0 = module_0.TimedOutException(*list_0)
        float_1 = 1056.94
        timed_out_exception_1 = module_0.TimedOutException()
        str_1 = '<A5V'
        bytes_0 = b'\xe00\xbaN\x07R\xd5\xbc\x127\x11l\xc0^\xa7\x90\x1c\t'
        action_module_0 = module_0.ActionModule(list_0, timed_out_exception_1, list_0, str_1, float_1, bytes_0)
        int_0 = 438
        bool_0 = None
        list_1 = [bool_0, timed_out_exception_1, int_0]
        str_2 = 'cPE^\rH~HN\r/xxkR;.'
        str_3 = '\n    name: junit\n    type: aggregate\n    short_description: write playbook output to a JUnit file.\n    version_added: historical\n    description:\n      - This callback writes playbook output to a JUnit formatted XML file.\n      - "Tasks show up in the report as follows:\n        \'ok\': pass\n        \'failed\' with \'EXPECTED FAILURE\' in the task name: pass\n        \'failed\' with \'TOGGLE RESULT\' in the task name: pass\n        \'ok\' with \'TOGGLE RESULT\' in the task name: failure\n        \'failed\' due to an exception: error\n        \'failed\' for other reasons: failure\n        \'skipped\': skipped"\n    options:\n      output_dir:\n        name: JUnit output dir\n        default: ~/.ansible.log\n        description: Directory to write XML files to.\n        env:\n          - name: JUNIT_OUTPUT_DIR\n      task_class:\n        name: JUnit Task class\n        default: False\n        description: Configure the output to be one class per yaml file\n        env:\n          - name: JUNIT_TASK_CLASS\n      task_relative_path:\n        name: JUnit Task relative path\n        default: none\n        description: Configure the output to use relative paths to given directory\n        version_added: "2.8"\n        env:\n          - name: JUNIT_TASK_RELATIVE_PATH\n      fail_on_change:\n        name: JUnit fail on change\n        default: False\n        description: Consider any tasks reporting "changed" as a junit test failure\n        env:\n          - name: JUNIT_FAIL_ON_CHANGE\n      fail_on_ignore:\n        name: JUnit fail on ignore\n        default: False\n        description: Consider failed tasks as a junit test failure even if ignore_on_error is set\n        env:\n          - name: JUNIT_FAIL_ON_IGNORE\n      include_setup_tasks_in_report:\n        name: JUnit include setup tasks in report\n        default: True\n        description: Should the setup tasks be included in the final report\n        env:\n          - name: JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT\n      hide_task_arguments:\n        name: Hide the arguments for a task\n        default: False\n        description: Hide the arguments for a task\n        version_added: "2.8"\n        env:\n          - name: JUNIT_HIDE_TASK_ARGUMENTS\n      test_case_prefix:\n        name: Prefix to find actual test cases\n        default: <empty>\n        description: Consider a task only as test case if it has this value as prefix. Additionaly failing tasks are recorded as failed test cases.\n        version_added: "2.8"\n        env:\n          - name: JUNIT_TEST_CASE_PREFIX\n    requirements:\n      - enable in configuration\n'
        bool_1 = False
        tuple_0 = (list_1, bool_1)
        set_0 = set()
        bytes_1 = b':5\x81q.\xa1\x94f\r\xa6'
        action_module_1 = module_0.ActionModule(list_1, str_3, action_module_0, tuple_0, set_0, bytes_1)
        var_0 = action_module_1.do_until_success_or_timeout(dict_0, int_0, action_module_0, str_2)
        list_2 = [bool_0, float_1, float_1]
        action_module_2 = module_0.ActionModule(str_1, int_0, bool_0, list_1, list_2, bytes_0)
        list_3 = [action_module_0, str_1, action_module_0, action_module_2]
        dict_1 = {list_3: int_0}
        list_4 = [dict_1, int_0, list_1]
        bytes_2 = b'\xfe\xdcY\x82\xa8`\xaa"\xcdF'
        action_module_3 = module_0.ActionModule(list_4, bool_0, bool_0, bytes_2, list_2, bytes_0)

if __name__ == "__main__":
    unittest.main()
