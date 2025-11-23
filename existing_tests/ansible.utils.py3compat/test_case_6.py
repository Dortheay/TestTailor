import unittest
import timeout_decorator
import ansible.utils.py3compat as module_0

class Test_Py3compat_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        bool_0 = False
        str_0 = "\n    Walk a filesystem tree returning enough information to copy the files\n\n    :arg topdir: The directory that the filesystem tree is rooted at\n    :kwarg base_path: The initial directory structure to strip off of the\n        files for the destination directory.  If this is None (the default),\n        the base_path is set to ``top_dir``.\n    :kwarg local_follow: Whether to follow symlinks on the source.  When set\n        to False, no symlinks are dereferenced.  When set to True (the\n        default), the code will dereference most symlinks.  However, symlinks\n        can still be present if needed to break a circular link.\n    :kwarg trailing_slash_detector: Function to determine if a path has\n        a trailing directory separator. Only needed when dealing with paths on\n        a remote machine (in which case, pass in a function that is aware of the\n        directory separator conventions on the remote machine).\n    :returns: dictionary of tuples.  All of the path elements in the structure are text strings.\n            This separates all the files, directories, and symlinks along with\n            important information about each::\n\n                { 'files': [('/absolute/path/to/copy/from', 'relative/path/to/copy/to'), ...],\n                  'directories': [('/absolute/path/to/copy/from', 'relative/path/to/copy/to'), ...],\n                  'symlinks': [('/symlink/target/path', 'relative/path/to/copy/to'), ...],\n                }\n\n        The ``symlinks`` field is only populated if ``local_follow`` is set to False\n        *or* a circular symlink cannot be dereferenced.\n\n    "
        text_environ_0 = module_0._TextEnviron(str_0)
        var_0 = text_environ_0.__getitem__(bool_0)

if __name__ == "__main__":
    unittest.main()
