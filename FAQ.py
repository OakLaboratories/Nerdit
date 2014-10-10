#!/usr/bin/python
print 'Content-type:text/html\n'
import cgi
import cgitb
import data
cgitb.enable()

###To copy over the text
form = cgi.FieldStorage()
fle = open('FAQ.html')
txt = fle.read()
fle.close
if 'usr' not in form or 'password' not in form:
    print txt
    print '<h1><a href="index.html"> Login!!</a></h1>'
else:
    ###To copy the user's information
    usr = form['usr'].value
    password = form['password'].value
    level = form['level'].value

    ###To create the file
    print txt
    print "<form action='home.py' method='POST'><input type='hidden' name='usr' value='" + usr + "'><input type='hidden' name='password' value='" + password + "'><input type='hidden' name='level' value='" + level + "'>"
    print '<input type="submit" value="Return to Homepage"  name="home" class="linkbutton"></form>'
