import subprocess
serverIP = raw_input('Enter server ip addr: ')
ntpIP = raw_input('Enter server ip addr: ')
bashCommand = 'uemcli -d ' + ip + ' /net/ntp/server create -server ' + ntpIP
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print('Output: {output}'.format(output=output))
print(type(output))
if 'Operation completed successfully' in output:
    print('Success')
print('Error: {error}'.format(error=error))