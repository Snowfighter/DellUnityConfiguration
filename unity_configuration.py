'''
Parameters needed
General:
* unity default password
* new admin password
* san netmask
* san gateway
* new_admin user
* new_admin password
* ntp server number
* ntp server ips
Unity Specific
* ip
* unity name
* path to lic
'''
import subprocess
import os
import re
from uemcli_commands import *


class Unity():
    unity_default_password = 'Password123#'

    def __init__(self, sanNetmask='', sanGateway='', adminPassword='', newAdminUser='', newAdminUserPassword='', ntpIPs = [], unityIP='', unityName='', pathToLic=''):
        self.sanNetmask = sanNetmask
        self.sanGateway = sanGateway
        self.adminPassword = adminPassword
        self.newAdminUser = newAdminUser
        self.newAdminUserPassword = newAdminUserPassword
        self.ntpIPs = ntpIPs
        self.unityIP = unityIP
        self.unityName = unityName
        self.pathToLic = pathToLic

    def __str__(self):
        return "\nUnity Name: {unityName}\n \
                Unity IP Address: {unityIP}\n \
                Path to License File: {pathToLic}\n \
                SAN Gateway: {sanGateway}\n \
                SAN Netmask: {sanNetmask}\n \
                Admin Password: {adminPassword}\n \
                New Administration User's Name: {newAdminUser}\n \
                {newAdminUser} Password: {newAdminUserPassword}\n \
                NTP Servers: {ntpIPs}".format(unityName = self.unityName, unityIP = self.unityIP, \
                    pathToLic = self.pathToLic, sanGateway = self.sanGateway, sanNetmask = self.sanNetmask, \
                    adminPassword = self.adminPassword, newAdminUser = self.newAdminUser, newAdminUserPassword = self.newAdminUserPassword, \
                    ntpIPs = self.ntpIPs)


def validateIPMask(mask):
    octets = mask.split('.')
    return len(octets) == 4 and all(i.isdigit() and 0 <= int(i) <= 256 for i in octets)


def validatePassword(password):
    if len(password) < 8:
        print("Your password's length should me at least 8 symbols!")
        return False
    elif re.search('[0-9]', password) is None:
        print("Your password should contain at least one number!")
        return False
    elif re.search('[A-Z]', password) is None:
        print("Your password should contain at least one capital letter!")
        return False
    elif re.search('[@_!#$%^&*()<>?/\|}{~:]', password) is None:
        print("Your password should contain at least one special character!")
        return False
    else:
        return True


def unityGeneralConfiguration(unity):
    # Asking for SAN Gateway
    while True:
        sanGateway = raw_input("Enter the valid SAN Gateway IP address [192.168.0.1]: ")
        if validateIPMask(sanGateway):
            unity.sanGateway = sanGateway
            break
        else:
            print('Enter valid IP!')
            continue

    # Asking for a san Netmask
    while True:
        sanNetmask = raw_input("Enter valid SAN Netmask [255.255.255.0]: ")
        if validateIPMask(sanNetmask):
            unity.sanNetmask = sanNetmask
            break
        else:
            print('Enter valid Mask!')
            continue

    # Asking for new Admin password
    while True:
        adminPassword = raw_input("Enter updated Admin password: ")
        if validatePassword(adminPassword):
            unity.adminPassword = adminPassword
            break
        else:
            continue

    # Asking for new administration User name
    newAdminUser = raw_input("Enter new administration user's name: ")
    unity.newAdminUser = newAdminUser
    
    # Asking for new administration User password
    while True:
        newAdminUserPassword = raw_input("Enter new administration user's password: ")
        if validatePassword(newAdminUserPassword):
            unity.newAdminUserPassword = newAdminUserPassword
            break
        else:
            continue

    # Asking for ntp servers' IP addresses
    while True:
        ntpNum = raw_input("Enter the number of NTP servers you wish to use [1-9]: ")
        try:
            ntpNum = int(ntpNum)
            break
        except ValueError:
            print('Enter the right number!')
            continue

    for _ in range(ntpNum):
        while True:
            ip = raw_input("Enter the NTP server IP address [192.168.0.1]: ")
            if validateIPMask(ip):
                unity.ntpIPs.append(ip)
                break
            else:
                print('Enter valid IP!')
                continue
    

def unitySpecificConfiguration(unity):
    # Asking for Unity IP
    while True:
        unityIP = raw_input("Enter the valid Unity IP address [192.168.0.1]: ")
        if validateIPMask(unityIP):
            unity.unityIP = unityIP
            break
        else:
            print('Enter valid IP!')
            continue
    
    # Asking for Unity Name
    unityName = raw_input("Enter the valid Unity Name [enm/eniq/ombs_X_unity]: ")
    unity.unityName = unityName
    
    # Asking for license file
    while True:
        pathToLic = raw_input("Enter the path to Unity License file [/var/tmp/unity.lic]: ")
        if os.path.isfile(pathToLic):
            unity.pathToLic = pathToLic
            break
        else:
            print('File does not exist!')
            continue


def main():

    unity = Unity()
    unityGeneralConfiguration(unity)

    # Asking the user for the number of Unities
    while True:
        numOfUnity = raw_input("Number of Unities in the deployment [1-9, q]: ")
        if numOfUnity == 'q':
            print('Script is quiting ...')
            return
        else:
            try:
                numOfUnity = int(numOfUnity)
                break
            except ValueError:
                print('Enter the right number!')
                continue

    # Executing configuration on Unities
    for _ in range(numOfUnity):
        unitySpecificConfiguration(unity)
        # Promting to check if the information is correct
        print('############################')
        print('Configuration')
        print('############################')
        print(unity)
        while True:
            configCheck = raw_input('Is this configuration correct [y/n]: ')
            if configCheck == 'y':
                break
            elif configCheck == 'n':
                return
            else:
                print('Type y or n!')
                continue


        

if __name__ == "__main__":
    main()