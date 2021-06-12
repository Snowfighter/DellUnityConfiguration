import subprocess
ip = raw_input('Enter ip addr: ')
bashCommand = 'uemcli -d ' + ip + ' /net/ntp/server show detail'
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print('Output: {output}'.format(output=output))
print('Error: {error}'.format(error=error))