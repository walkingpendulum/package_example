# palindrome_checker
Here are some information about the package.

Palindrome checker is an example made to demonstrate the concepts of python package development and distribution.

### Package development

To install requirements run `make init`.

To test package run `make test`.

To install package to your system in editable mode run `pip install -e .` command. After that pip will add symlink to your package into your PYTHONAPTH and paths to entrypoint scripts to your PATH, so you can run your binaries (if present) from shell.

Do not forget to extend CHANGELOG.md.

### Package binaries usage
Check script version:
```bash
$ check_palindrome --version
check_palindrome 0.1.0
```

Run and check result code: 
```bash
$ check_palindrome -i aaa
$ echo $?
0
$ check_palindrome -i aab
$ echo $?
1
```

### Bash autocompletion
To enabling bash autocompletion execute
```bash
echo 'eval "$(register-python-argcomplete check_palindrome)"' >> ~/.bash_profile
``` 
