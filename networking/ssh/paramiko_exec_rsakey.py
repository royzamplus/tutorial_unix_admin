#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Connecting to an SSH server and remotely executing a command

import paramiko

hostname = '192.168.0.1'
port = 22
username = 'tom'
pkey_file = '/home/tom/.ssh/id_rsa'

if __name__ == '__main__':
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username=username, pkey=key)
    stdin, stdout, stderr = s.exec_command('uname -a')
    print stdout.read()
    s.close()