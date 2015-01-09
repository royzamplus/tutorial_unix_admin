#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pwd

print pwd.getpwnam('roy')

shell = pwd.getpwnam('roy')[-1]

print shell