from subprocess import PIPE, Popen
import subprocess
# You can start a process in Python using the Popen function call. The program below starts the
# unix program ‘cat’ and the second parameter is the argument. This is equivalent to ‘cat test.py’.
# You can start any program with any parameter.

#process = Popen(["ls", "-l"], stdout=PIPE, stderr=PIPE)
process = Popen(["ls", "-l"], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stdout)
#print(stderr)

# The process.communicate() call reads input and output from the process.  stdout is the process
# output. stderr will be written only if an error occurs.  If you want to wait for the program
# to finish you can call Popen.wait().

print("============================================================================================")

# Subprocess has a method call() which can be used to start a program. The parameter is a list of
# which the first argument must be the program name.
subprocess.call(["ls", "-l"])

print("============================================================================================")

# We can get the output of a program and store it in a string directly using check_output

output = subprocess.check_output(["echo", "process"])
print(str(output))

print("============================================================================================")