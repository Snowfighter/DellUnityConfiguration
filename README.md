<img src='./media/unity_automatization_logo.png' alt='Dell EMC Unity Automatization' title='Dell EMC Unity Automatization'/>

# Dell EMC Unity Configuration

[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)]
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

The idea of creating this script came to me while working on a project at my job.

## Overview
The specifics of the initial configuration of Dell Unity in the deployments I am working with is that it has to be assigned a temporary address and then be configured via a series of `uemcli` commands. 

## Problem
If the deployment has several Unities (and it usually has), it may become really tedious and unproductive to type the commands for each Unity over and over again. Unfortunately, the lifespan of the temporary address is very short, so you need to be quick at executing `uemcli` commands, which can lead to errors. 

## Solution
The solution for this problem was implemented in [unity_configuration](./unity_configuration.py). The main parts of this script are `Unity` class, `unityGeneralConfiguration` function, `unitySpecificConfiguration` function and `main` function.

### `Unity` Class
This class is used for creating objects that store general information about the deployment itself and certain specifics about a Unity. Here is the list of attributes:

**General**:

- `sanNetmask` - SAN Netmask (*string*)
- `sanGateway` - SAN Gateway (*string*)
- `adminPassword` - New Admin password to use instead of the default (*string*)
- `newAdminUser` - Another User with admin privileges (*string*)
- `newAdminUserPassword` - Password related to the User in the previous point (*string*)
- `ntpIPs` - List of NTP servers (*list*)

**Specifics**:

- `unityIP` - Specific Unity IP Address (*string*)
- `unityName` - Specific Unity Name (*string*)
- `pathToLic` - Path to the License File (*string*)

### `unityGeneralConfiguration` Function
This function receives a `Unity` object and populates it with the general information about the deployment.

Every inputed IP and Mask is validated via `validateIPMask` function and passwords are validated via `validatePassword` function.

### `unitySpecificConfiguration` Function
This function is executed for every Unity in the deployment to gather specific information about particular Unity.

Every inputed IP and Mask is validated via `validateIPMask` function and passwords are validated via `validatePassword` function.

### `main` Function

1. This function gathers general information about the deployment. 
2. It receives the number of Unities in the deployment
3. For every Unity the specific infromation is gathered and all the parameters are printed out for confirmation
4. A series of `uemcli` commands are executed after confirmation. These commands are described in [uemcli_commands](./uemcli_commands.py) file.

# Usage

1. Provide general information about the deployment.
2. Specify the number of Unities
3. Provide Information for *N* Unity
4. Confirm the overall information about *N* Unity
5. For every `uemcli` command confirm its execution
6. If the `uemcli` command failed the script quits
7. Repeat steps [3-6] for every Unity

# Additional Info


