from subprocess import Popen, PIPE

process = Popen(['ping','8.8.8.8','-n','2'], shell=True, stdout=PIPE, stderr=PIPE)

print (process.stdout.read())
rc = process.wait()
print("exit code: {}".format(rc))

print("error: {}".format(process.stderr.read()))
