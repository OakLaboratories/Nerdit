#!/usr/bin/python
print 'Content-type:text/html\n'

import cgi
import cgitb
import hashlib
import data
cgitb.enable()
    
def check(usr, password):
    """Checks if the username and password are correct, returning a string to print about it"""
    d = data.namedict()
    if usr in d:
        if d[usr][0] == password:
            return "<h1>Username and Password Correct.</h1><form method='POST' action='trivia.py'>" + userdata + "<input class='linkbutton' type='submit' name='submit' value='Click to Advance Further'></form>"
    return "<h1>Username and Password Incorrect.</h1><a href='index.html'>Click to go Back</a>"

def register(usr, password, confirm):
    """Adds to the names.txt file the new info after checking if confirm is the same as password"""
    if confirm != password:
        return "<h1>Passwords not the same!</h1><a href='register.html'>Please try again</a>"
    else:
        d = data.namedict()
        if usr in d:
            return"<h1>Username Taken.</h1><a href='index.html'>Click to go Back</a>"
        else:
            f = open('names.txt', 'a')
            f.write(usr + '@%' + password + '@%1\n')
            f.close()
            return "<h1>Registration Complete.</h1><form method='POST' action='trivia.py'>" + userdata + "<input class='linkbutton' type='submit' name='submit' value='Click to Advance Further'></form>"

d = cgi.FieldStorage()
print '<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body>'
if 'usr' in d.keys() and 'password' in d.keys():
    usr = data.check(d['usr'].value)
    password = d['password'].value
    password = hashlib.md5(password).hexdigest()
    if 'confirm' in d.keys():
        confirm = d['confirm'].value
        confirm = hashlib.md5(confirm).hexdigest()
    userdata = "<input type='hidden' name='usr' value='" + usr + "'><input type='hidden' name='password' value=" + password + ">"
    if 'login' in d.keys():
        print check(usr, password)
    elif 'register' in d.keys():
        print register(usr, password, confirm)
else:
    print "<h1>Username and Password Incorrect.</h1><a href='index.html'>Click to go Back</a>"
print '</body></html>'
