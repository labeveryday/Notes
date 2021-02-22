# Bash Notes

A shell is an interface that a user leverages to communicate with the operating system. The shell enables you to manipulate files, run commands, utilities, programs and more.

There are many different linux shells:

- [Korn shell](http://www.kornshell.org/)
- [Z shell](https://www.zsh.org/)
- C shell
- [Bourne-again shell `Bash`](https://www.gnu.org/software/bash/https://www.gnu.org/software/bash/)

## Executing bash scripts

When you create a shell script there a couple of things to note:

1. At the top of your script you need to tell the operating system which interpreter to us to execute the script. You do this by entering a shebang
`#! /bin/bash`

2. Save your file as `filename.sh`

> NOTE: the `.sh` is not required to execute your script

3. Next you have to give yourself execute permissions of the python script.

```bash
ls -l
chmod 755 <filename.sh>
```

4. To execute your script in the shell:

`./<filename>`

### Built-in Bash Commands

| Commands                                          | Description                                               |
| -------------                                     | :-------------                                           |
:   | Returns 0 or true
.   | Executes a shell script
bg  | Puts a job in the background
cd  | Changes directory
continue    | Resumes the current loop
echo    | Displays the command arguments
eval    | Evaluates the following expression
exec    | Executes the following command without creating a new process, replacing the current process
exit    | Quits the shell
export  | Makes a variable of function available to other programs that are executed from this shell
fg      | Brings a job to the foreground
getopts | Parses arguments to the shell script
jobs    | Lists background (bg) jobs
pwd     | Displays the current directory
read    | Reads a line from standard input
readonly | Declares a variable as read-only
set     | Lists all variables
shift   | Moves the script's input parameters to the left, dropping the first parameter (useful for consuming all parameters one at a time)
test    | Evaluates arguments
[[      | Performs a conditional test
times   | Prints the user and system times
trap    | Traps a signal so the script can handle it (untrapped signals terminate the script)
type    | Displays how each argument would be interpreted as a command
unmask  | Changes the default permissions for a new file
wait    | Waits for a background process to complete
