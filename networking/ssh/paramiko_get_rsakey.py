#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Connecting to an SSH server and remotely executing a command

import os
import paramiko

hostname = '192.168.0.1'
port = 22
username = 'tom'
dir_path = '/home/tom/tmp'
pkey_file = '/home/tom/.ssh/id_rsa'

if __name__ == '__main__':
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print 'Retrieving', f
        sftp.get(os.path.join(dir_path, f), f)
    t.close()