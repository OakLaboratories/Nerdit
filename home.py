#!/usr/bin/python
print 'Content-type:text/html\n'

import cgi
import cgitb
cgitb.enable()
import data

def showLink(usr):
    """Returns a string containing the table of links to each page to be printed"""
    form = ""
    lst = data.subsplit('posts.txt', '@%')
    count = 0
    likelist = []
    while count < len(lst):
        item = []
        item.append(lst[count][1])
        item.append(data.countLike(lst[count][1]))
        likelist.append(item)
        count += 1
    forms = "<table border=1><tr><th>Title</th><th>Likes</th><th>Creator</th><th>Datetime</th></tr>"
    while len(likelist) > 0:
        n = maxLike(likelist)
        forms += "<tr>"
        forms += "<td><form action='pageform2.py' style='display:inline;' method='GET'>" + userdata
        forms += "<input type='hidden' name='n' value=" + lst[int(n)-1][1] + ">"
        forms += "<input type='submit' name='display' class='linkbutton' value='" + data.htmlcheck(lst[int(n)-1][0]) + "'></form></td><td>" + str(data.countLike(n)) + "</td><td>" + lst[int(n)-1][2] + "</td><td>" + lst[int(n)-1][4] +"</td></tr>"
        forms += "</tr>"
        entry = []
        entry.append(n)
        entry.append(data.countLike(n))
        likelist.remove(entry)
    forms += "</table>"
    return forms
        
def maxLike(lst):
    """Returns the page number with the maximum number of likes, so it can be printed first"""
    x = lst[0][1]
    n = lst[0][0]
    count = 0
    while count < len(lst):
        if (int(lst[count][1]) > int(x)) or (int(lst[count][1]) == int(x) and lst[count][0] > n):
            x = lst[count][1]
            n = lst[count][0]
        count += 1
    return n

d = cgi.FieldStorage()
if 'usr' not in d or 'password' not in d or 'level' not in d:
    print '<html><head><title>Nerdit</title></head><link rel="stylesheet" type="text/css" href="nerdit.css"><body><center><a href=index.html>Userdata Not Found</a></center></body></html>'
else:
    level = d['level'].value
    if level == '0':
        print '<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body><h1>You have been blocked from the site.</h1><br><a href=index.html>Click to go back to Login</a></body></html>'
    else:
        usr = d['usr'].value
        password = d['password'].value
        userdata = "<input type='hidden' name='usr' value='" + usr + "'><input type='hidden' name='password' value=" + password + "><input type='hidden' name='level' value=" + level + ">"
        print '<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body>'
        print "<h1><center>Welcome to Nerdit!</h1></center><br>" + showLink(usr)
        print "<br><center><b><form action='pageform2.py' method='GET'><input type='submit' name='make' class='linkbutton' value='Create Page'>"
        print userdata + "</form></b>"
        print """<b><form action='game.py' method='GET'>""" + userdata
        print """<input type='submit' name='game' value='The Word Game' class='linkbutton'></form>"""
        print """<form action='trials.py' method='GET'>""" + userdata + "<input name='qnumber' value='0' type='hidden'><input name='questionNumber' type='hidden' value='0'>"
        print """<input type='submit' name='trials' value='Raise Up Your Nerd Level' class='linkbutton'></form></b>"""
        print """<form action='FAQ.py' method='GET'>"""
        print userdata + """<b><input type='submit' name='FAQ' value="Woah, What's Going On Here?" class='linkbutton'></b></form>"""
        print "<b><a href='http://gdriv.es/oakenterprises'>Go to <i>Oak Enterprises</i></a></b>"        
        print "<br><br><b><a href='http://homer.stuy.edu/~alon.levin/final/Nerdit'>Logout</a></b></center>"
	if level == '5':
            print '<hr><h2>Admin Tools</h2>'
            print "<form action='admin.py' method='GET'>" + userdata + "<input type='text' required name='blockusr'><input type='submit' name='block' value='Block Users'></form>"
        print "</body></html>"


