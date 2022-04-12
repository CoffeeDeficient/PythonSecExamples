#!/usr/bin/python
import subprocess


print("subprocess call:\n")
result = subprocess.call(['ls', '-al'])
print(result)

print("\nsubprocess check_ouput:\n")
result = subprocess.check_output(['ls', '-al'])
print("Length of Result: %d"%len(result))
print("Print 3rd Line:")
print(result.split('\n')[2])

print("\nsubprocess Popen:\n")
phandle = subprocess.Popen(['ls','-al'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
result = phandle.stdout.read()
print("Length of Result: %d"%len(result))
print("Print 3rd Line:")
print(result.split('\n')[2])
