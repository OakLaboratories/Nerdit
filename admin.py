#!/usr/bin/python
print "content-type:text/html\n"

import random
import cgi
import cgitb
import data
import hashlib
cgitb.enable()

def admin(usr, adminpw):
    """Checks if the admin password is correct, and upgrades to level 5 if it is"""
    if hashlib.md5(adminpw).hexdigest()=='0963dbc909dbbecb9a1129370bb52e9e':
        lst = data.subsplit('names.txt', '@%')
        count = 0
        while count < len(lst):
            if lst[count][0] == usr:
                if lst[count][2] == '5':
                    print 'You are already the admin!'
                else:
                    lst[count][2] = '5'
                    f = open('names.txt', 'w')
                    ncount = 0
                    print 'Your level has been increased to 5, admin level!'
                    while ncount < len(lst):
                        f.write(lst[ncount][0] + '@%' + lst[ncount][1] + '@%' + lst[ncount][2] + '\n')
                        ncount += 1
                    level = '5'
            count += 1
        print "<br><form action='home.py' method='POST'><input type='hidden' name='usr' value=" + usr + "><input type='hidden' name='password' value=" + password + "><input type='hidden' name='level' value='5'>"
    else:
        print "You have failed. You will not be an admin!"
        print "<br><form action='home.py' method='POST'>" + userdata
    print "<input type='submit' class='linkbutton' name='home' value='Click to return to homepage'></form>"
    print data.footer

def block(usr):
    """Changes the level of usr to 0, such that they are blocked"""
    lst = data.subsplit('names.txt', '@%')
    count = 0
    found = ''
    while count < len(lst):
        if lst[count][0] == usr:
            if lst[count][2] == '5':
                found = 'admin'
            else:
                lst[count][2] = '0'
                found = 'True'
        count += 1
    count = 0
    f = open('names.txt', 'w')
    while count < len(lst):
        f.write(lst[count][0] + '@%' + lst[count][1] + '@%' + lst[count][2] + '\n')
        count += 1
    f.close()
    if found == 'True':
        return '<h1>User deleted</h1>'
    elif found == 'admin':
        return '<h1>User is an admin</h1>'
    else:
        return '<h1>User does not exist</h1>'

inputs = cgi.FieldStorage()
if 'usr' not in inputs or 'password' not in inputs or 'level' not in inputs:
    print '<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body><center><a href=index.html>Userdata Not Found</a></center></body></html>'
else:
    level = inputs['level'].value
    if level == '0':
        print '<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body><h1>You have been blocked from the site.</h1><br><a href=index.html>Click to go back to Login</a></body></html>'
    else:
        print data.header
        usr = inputs['usr'].value
        password = inputs['password'].value
        userdata = "<input type='hidden' name='usr' value=" + usr + "><input type='hidden' name='password' value=" + password + "><input type='hidden' name='level' value=" + level + ">"
        if 'adminpw' in inputs:
            adminpw = inputs['adminpw'].value
            admin(usr, adminpw)
        if 'block' in inputs:
            print data.header
            blockusr = inputs['blockusr'].value
            print block(blockusr)
            print "<form action='home.py' method='POST'><input type='submit' class='linkbutton' name='home' value='Return to Homepage'>" + userdata + '</form>'
            print data.footer

