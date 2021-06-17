<img src='./media/unity_automatization_logo.png' alt='Dell EMC Unity Automatization' title='Dell EMC Unity Automatization'/>

# Dell EMC Unity Configuration

The idea of creating this script came to me while working on a project at my job.

## Overview
The specifics of the initial configuration of Dell Unity in the deployments I am working with is that it has to be assigned a temporary address and then be configured via a series of `uemcli` commands. 

## Problem
If the deployment has several Unities (and it usually has), it may become really tedious and unproductive to type the commands for each Unity over and over again. Unfortunately, the lifespan of the temporary address is very short, so you need to be quick at executing `uemcli` commands, which can lead to errors. 

## Solution
The solution for this problem was implemented in [unity_configuration](./unity_configuration.py)
