import unittest
import timeout_decorator
import ansible.plugins.shell.powershell as module_0

class Test_Powershell_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            shell_module_0 = module_0.ShellModule()
            str_0 = '\n- name: Change file ownership, group and permissions\n  ansible.builtin.file:\n    path: /etc/foo.conf\n    owner: foo\n    group: foo\n    mode: \'0644\'\n\n- name: Give insecure permissions to an existing file\n  ansible.builtin.file:\n    path: /work\n    owner: root\n    group: root\n    mode: \'1777\'\n\n- name: Create a symbolic link\n  ansible.builtin.file:\n    src: /file/to/link/to\n    dest: /path/to/symlink\n    owner: foo\n    group: foo\n    state: link\n\n- name: Create two hard links\n  ansible.builtin.file:\n    src: \'/tmp/{{ item.src }}\'\n    dest: \'{{ item.dest }}\'\n    state: hard\n  loop:\n    - { src: x, dest: y }\n    - { src: z, dest: k }\n\n- name: Touch a file, using symbolic modes to set the permissions (equivalent to 0644)\n  ansible.builtin.file:\n    path: /etc/foo.conf\n    state: touch\n    mode: u=rw,g=r,o=r\n\n- name: Touch the same file, but add/remove some permissions\n  ansible.builtin.file:\n    path: /etc/foo.conf\n    state: touch\n    mode: u+rw,g-wx,o-rwx\n\n- name: Touch again the same file, but do not change times this makes the task idempotent\n  ansible.builtin.file:\n    path: /etc/foo.conf\n    state: touch\n    mode: u+rw,g-wx,o-rwx\n    modification_time: preserve\n    access_time: preserve\n\n- name: Create a directory if it does not exist\n  ansible.builtin.file:\n    path: /etc/some_directory\n    state: directory\n    mode: \'0755\'\n\n- name: Update modification and access time of given file\n  ansible.builtin.file:\n    path: /etc/some_file\n    state: file\n    modification_time: now\n    access_time: now\n\n- name: Set access time based on seconds from epoch value\n  ansible.builtin.file:\n    path: /etc/another_file\n    state: file\n    access_time: \'{{ "%Y%m%d%H%M.%S" | strftime(stat_var.stat.atime) }}\'\n\n- name: Recursively change ownership of a directory\n  ansible.builtin.file:\n    path: /etc/foo\n    state: directory\n    recurse: yes\n    owner: foo\n    group: foo\n\n- name: Remove file (delete file)\n  ansible.builtin.file:\n    path: /etc/foo.txt\n    state: absent\n\n- name: Recursively remove directory\n  ansible.builtin.file:\n    path: /etc/foo\n    state: absent\n\n'
            dict_0 = {}
            var_0 = shell_module_0.remove(str_0, dict_0)
            bytes_0 = b'\x96(/\xe7\xe5<\x08><\x12)\xfbr\xdc\xbb\xcf\x01\xfa\r'
            shell_module_1 = module_0.ShellModule()
            var_1 = shell_module_1.mkdtemp(shell_module_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
