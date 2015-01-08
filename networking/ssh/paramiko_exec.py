#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Connecting to an SSH server and remotely executing a command

import paramiko

hostname = '192.168.0.1'
port = 22
username = 'tom'
password = 'xxx'

if __name__ == '__main__':
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('uname -a')
    print stdout.read()
    s.close()