#!/usr/bin/python

print "content-type:text/html\n"

import random
import cgi
import cgitb
import data
cgitb.enable()

def send(inputs):
    f = open('nerd.txt')
    s = f.read()
    f.close()
    s = s.split('\n')
    s = s[int(questionNumber)]
    s = s.split('%@')
    if s[1] in inputs:
        print 'Congratulations. You have been granted level <b>' + level + '</b> access to Nerdit. <b>Happy Nerding</b>!'
        access = "<br>"
        if level == '0':
            access += 'You have been trapped, as you left us, buried alive, buried alive. No access for you!'
            access += '<a href="index.html">Click to go back to the login page</a>'
        else:
            if level == '1':
                access += 'The answer to life, the universe, and everything is... viewing this site!<br>Welcome and enjoy!'
            elif level == '2':
                access += 'The line must be drawn here, this far, no further. And I must like or dislike them for what they have done!'
            elif level == '3':
                access += 'I have been and always shall be allowed to like, dislike, and comment.<br>Now you are too!'
            elif level == '4':
                access += 'You do not have the authority to deny return of the ability to post on the site!<br>You are granted it!'
            elif level == '5':
                access = '<h1> Welcome Lord Administrator, King on the Nerdit Throne! </h1>'
            access += """<form action="home.py" method="POST"><br>
            <input type="submit" class='linkbutton' name="nerd" value="Proceed to Nerdit">""" + userdata
            access += '</form>'
        print access
    else:
        print 'You have brought shame and dishonor upon your family.'
        print """<form action="trivia.py" method="POST"><br><input class='linkbutton' type='submit' name='back' value='Retake Quiz'>"""
        print userdata + '</form>'
inputs = cgi.FieldStorage()



if 'usr' not in inputs or 'password' not in inputs or 'level' not in inputs:
    print '<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body><center><a href=index.html>Userdata Not Found</a></center></body></html>'
else:
    level = inputs['level'].value
    if level == '0':
        print '<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body><h1>You have been blocked from the site.</h1><br><a href=index.html>Click to go back to Login</a></body></html>'
    else:
        questionNumber = inputs['questionNumber'].value
        usr = inputs['usr'].value
        password = inputs['password'].value
        userdata = "<input type='hidden' name='usr' value='" + usr + "'><input type='hidden' name='password' value=" + password + "><input type='hidden' name='level' value='" + level + "'>"
        print'<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body>'
        print '<h1>Are you really ready for Nerdit, ' + usr + '?</h1>'
        send(inputs)
        print "</body></html>"

