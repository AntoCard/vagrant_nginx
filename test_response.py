#!/usr/bin/env python

import urllib2
import socket

app_servers = [
               '192.168.1.44',
               '192.168.1.45',
               '192.168.1.46'
               ]

string = "Hello World!"

timeout = 5
socket.setdefaulttimeout(timeout)

for server in app_servers:
    try:
        response = urllib2.urlopen("http://" + server).read()
        if response == string:
            print "server " + server + " running app"
        else:
            print "server " + server + " not ok"
    except:
        print "Something went wrong with " + server
