import unittest
import timeout_decorator
import ansible.playbook.helpers as module_0

class Test_Helpers_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = ''
            str_1 = 'action'
            str_2 = 'msg'
            str_3 = 'task1'
            str_4 = '\n        Execute a command, returns rc, stdout, and stderr.\n\n        :arg args: is the command to run\n            * If args is a list, the command will be run with shell=False.\n            * If args is a string and use_unsafe_shell=False it will split args to a list and run with shell=False\n            * If args is a string and use_unsafe_shell=True it runs with shell=True.\n        :kw check_rc: Whether to call fail_json in case of non zero RC.\n            Default False\n        :kw close_fds: See documentation for subprocess.Popen(). Default True\n        :kw executable: See documentation for subprocess.Popen(). Default None\n        :kw data: If given, information to write to the stdin of the command\n        :kw binary_data: If False, append a newline to the data.  Default False\n        :kw path_prefix: If given, additional path to find the command in.\n            This adds to the PATH environment variable so helper commands in\n            the same directory can also be found\n        :kw cwd: If given, working directory to run the command inside\n        :kw use_unsafe_shell: See `args` parameter.  Default False\n        :kw prompt_regex: Regex string (not a compiled regex) which can be\n            used to detect prompts in the stdout which would otherwise cause\n            the execution to hang (especially if no input data is specified)\n        :kw environ_update: dictionary to *update* environ variables with\n        :kw umask: Umask to be used when running the command. Default None\n        :kw encoding: Since we return native strings, on python3 we need to\n            know the encoding to use to transform from bytes to text.  If you\n            want to always get bytes back, use encoding=None.  The default is\n            "utf-8".  This does not affect transformation of strings given as\n            args.\n        :kw errors: Since we return native strings, on python3 we need to\n            transform stdout and stderr from bytes to text.  If the bytes are\n            undecodable in the ``encoding`` specified, then use this error\n            handler to deal with them.  The default is ``surrogate_or_strict``\n            which means that the bytes will be decoded using the\n            surrogateescape error handler if available (available on all\n            python3 versions we support) otherwise a UnicodeError traceback\n            will be raised.  This does not affect transformations of strings\n            given as args.\n        :kw expand_user_and_vars: When ``use_unsafe_shell=False`` this argument\n            dictates whether ``~`` is expanded in paths and environment variables\n            are expanded before running the command. When ``True`` a string such as\n            ``$SHELL`` will be expanded regardless of escaping. When ``False`` and\n            ``use_unsafe_shell=False`` no path or variable expansion will be done.\n        :kw pass_fds: When running on Python 3 this argument\n            dictates which file descriptors should be passed\n            to an underlying ``Popen`` constructor. On Python 2, this will\n            set ``close_fds`` to False.\n        :kw before_communicate_callback: This function will be called\n            after ``Popen`` object will be created\n            but before communicating to the process.\n            (``Popen`` object will be passed to callback as a first argument)\n        :kw ignore_invalid_cwd: This flag indicates whether an invalid ``cwd``\n            (non-existent or not a directory) should be ignored or should raise\n            an exception.\n        :returns: A 3-tuple of return code (integer), stdout (native string),\n            and stderr (native string).  On python2, stdout and stderr are both\n            byte strings.  On python3, stdout and stderr are text strings converted\n            according to the encoding and errors parameters.  If you want byte\n            strings on python3, use encoding=None to turn decoding to text off.\n        '
            str_5 = 'test1'
            str_6 = {str_0: str_3, str_1: str_4, str_2: str_5}
            str_7 = 'task2'
            str_8 = 'test2'
            str_9 = {str_0: str_7, str_1: str_4, str_2: str_8}
            str_10 = [str_9]
            str_11 = 'task3'
            str_12 = 'test3'
            str_13 = {str_0: str_11, str_1: str_4, str_2: str_12}
            str_14 = [str_6, str_10, str_13]
            str_15 = 'mocked_play'
            var_0 = None
            var_1 = None
            var_2 = None
            bool_0 = False
            var_3 = None
            var_4 = module_0.load_list_of_blocks(str_14, str_15, var_0, var_1, var_2, bool_0, str_6, var_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
