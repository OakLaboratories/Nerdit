#!/usr/bin/python
print 'Content-type:text/html\n'
import cgi
import cgitb
import data
cgitb.enable()

HTML_head = data.header + """
<center>
"""

fle = open('wordsEn.txt')
dictionary = fle.read()
fle.close

###Checks that the word is legal
def wordCheck(word, original):
    if word[0] == original[-1][0][-1] and word in dictionary:
        return True
    else:
        return False

###To create the table of last 20 entries
def current():
    lst = data.subsplit('words.txt', '@%')
    print '<table border=1><tr><th>Word</th><th>Writer</th><th>Date/Time</th></tr>'
    if len(lst) >= 20:
        ticker = len(lst) - 20
    else:
        ticker = 0
    while ticker < len(lst):
        print '<tr><td>' + lst[ticker][0] + '</td><td>' + lst[ticker][1] + '</td><td>' + lst[ticker][2] + '</td></tr>'
        ticker += 1
    return '</table><hr></font></center>'

###To enter the word into the database (if it is legal) or to show the rejection message
def submit(wrd, usr):
    print data.header
    txt = open('words.txt').read()
    open('words.txt').close()
    fle = open('words.txt', 'a')
    if wrd in txt:
        print """<font color="red"><h2><center>We're sorry, but that word has already been used. Try another one.</center></h2></font>"""
    elif not wordCheck(wrd, data.subsplit('words.txt', '@%')):
        print """<font color="red"><h2><center>We're sorry, but that word begins with a different letter than the last word ends with or is not a legal word. Try another one.</center></h2></font>"""
    else:
        fle.write(data.numbercheck(data.check(wrd)) + '@%' + usr + '@%' + data.timenow() + '\n')
        print """<font color="green"><h2><center>Thank you for your submission!</center></h2></font>"""
    print "<form action='game.py' method='POST'>" + userdata + "<input type='submit' class='linkbutton' value='Go Back' name='return'></form>"
    print data.footer
    fle.close()

###To reset the system via adding names to the voting list
def reset(usr, level):
        fle = open('reset.txt')
	txt = fle.read()
        fle.close()
	registry = open('reset.txt', 'a')
	if usr in txt and level != '5':
		print """<font color="red"><h2><center>We're sorry, but you cannot ask to reset the game more than once.</center></h2></font>"""
	else:
		registry.write(usr + '\n')
		print """<font color="blue"><h2><center>Thank you for your cooperation.</center></h2></font>"""
	ticker = 0
	mover = 0
	f = open('reset.txt')
	txt = f.read()
	f.close
	while ticker < 5 and mover < len(txt):
		if txt[mover] == '\n':
			ticker += 1
		mover += 1
	if ticker == 5 or level == '5':
		fle = open('words.txt', 'w')
		fle.write('apple@%' + usr + '@%' + data.timenow() + '\n')
		fle.close()
		fle = open('reset.txt', 'w')
		fle.close
		print """<font color="green"><h2><center>The game has been reset to default.</center></h2></font>"""	
	print "<form action='game.py' method='POST'>" + userdata + "<input type='submit' class='linkbutton' value='Close' name='return'></form>"

###To display the actual page
form = cgi.FieldStorage()
if 'new' in form:
    txt = form['new'].value
if 'usr' not in form or 'password' not in form or 'level' not in form:
    print '<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body><center><a href=index.html>Userdata Not Found</a></center></body></html>'
else:
    level = form['level'].value
    if level == '0':
        print '<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body><h1>You have been blocked from the site.</h1><br><a href=index.html>Click to go back to Login</a></body></html>'
    else:
        usr = form['usr'].value
        password = form['password'].value
        userdata = "<input type='hidden' name='usr' value='" + usr + "'><input type='hidden' name='password' value=" + password + "><input type='hidden' name='level' value='" + level + "'>"
        if 'Submit' in form.keys():
            submit(txt, usr)
        else:
            print HTML_head
            print current()
            print '<font size="4">Would you like to submit a word?</font>'
            print '<form method="POST" action="game.py">'
            print '<input type="text" name="new" placeholder="Word" required>'
            print '<br><input type="submit" value="Submit Word" name="Submit">' + userdata + '</form>'
            print '<form method="POST" action="game.py"><input type="submit" value="Reset"  name="onceagain">' + userdata + '</form>'
            print '<form method="POST" action="home.py"><input type="submit" value="Return to Homepage"  name="home" class="linkbutton">' + userdata + '</form>'
        if 'onceagain' in form.keys():
            reset(usr, level)
        print data.footer

