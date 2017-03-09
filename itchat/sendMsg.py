#!/usr/bin/env python
import itchat
import sys
itchat.auto_login(hotReload=True)
itchat.send(sys.argv[1], toUserName=sys.argv[2])
