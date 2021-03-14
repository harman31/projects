#!/usr/bin/env python3
# Do not port scan for a URL you do not own
# Ports 8090, 80 or 443 to see if the message changes

import socket

s = socket.socket()

result = s.connect_ex(('YOUR_WEB_URL', 80))

if(result == 0):
    print('Port is open')
else:
    print('Port is closed')