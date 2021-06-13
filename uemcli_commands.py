# Execution Backbone
def execution(bashCommand, message):
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if 'error' not in output:
        print('##########')
        print(message)
        print('##########')
        print(output)
        return True
    else:
        print('##########')
        print(output)
        return False

# Accepting Licence Agreement 
def acceptingAgreement(unityIP, unity_default_password):    
    bashCommand = 'uemcli -d ' + unityIP + ' -u admin -p ' + unity_default_password + ' /sys/eula set -agree yes'
    message = 'Copyright License Agreement was accepted successfully'
    print(bashCommand)
    return execution(bashCommand, message)

# Change Password for Admin User
def changeAdminPassword(unityIP, unity_default_password, adminPassword):
    bashCommand = 'uemcli -d ' + unityIP + ' -u admin -p ' + unity_default_password + ' /user/account -id user_admin set -passwd ' + adminPassword + ' -oldpasswd ' + unity_default_password
    message = 'Admin password was successfully changed'
    print(bashCommand)
    return execution(bashCommand, message)

# Reassign Static IP
def assignStaticIP(unityIP, adminPassword, sanNetmask, sanGateway):
    bashCommand = 'uemcli -d ' + unityIP + ' -u admin -p ' + adminPassword + ' /net/if/mgmt set -ipv4 static -addr ' + unityIP + ' -netmask ' + sanNetmask + ' -gateway ' + sanGateway
    message = 'Static IP was assigned successfully'
    print(bashCommand)
    return execution(bashCommand, message)

# Assign Unity Name
def assignName(unityIP, adminPassword, unityName):
    bashCommand = 'uemcli -d ' + unityIP + ' -u admin -p ' + adminPassword + ' /sys/general set -name ' + unityName
    message = 'Assigned Unity Name successfully'
    print(bashCommand)
    return execution(bashCommand, message)

# Administration User Creation
def extraAdminUserCreation(unityIP, adminPassword, newAdminUser, newAdminUserPassword):
    bashCommand = 'uemcli -d ' + unityIP + ' -u admin -p ' + adminPassword + ' /user/account create -name ' + newAdminUser + ' -type local -passwd ' + adminPassword + ' -role administrator'
    message = newAdminUser + ' was created successfully'
    print(bashCommand)
    return execution(bashCommand, message)

# User Security File Creation
def securityFileCreation(unityIP, adminPassword):
    bashCommand = 'uemcli -d ' + unityIP + ' -u admin -p ' + adminPassword + ' -saveUser'
    message = ' Security File was created successfully'
    print(bashCommand)
    return execution(bashCommand, message)

# Configuring Time Services
def configureNTP(unityIP, ntpIPs):
    for ip in ntpIPs:
        bashCommand = 'uemcli -d ' + unityIP +  ' /net/ntp/server create -server ' + ip
        message = ip + ' was successfully added'
        print(bashCommand)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        if 'error' not in output:
            print(message)
        else:
            print(output)
            return False

# Install License
def license(unityIP, pathToLic):
    bashCommand = 'uemcli -d ' + unityIP + ' -upload -f ' + pathToLic + ' license'
    message = 'License was successfully installed'
    print(bashCommand)
    return execution(bashCommand, message)


    