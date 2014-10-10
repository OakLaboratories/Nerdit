#!/usr/bin/python

print "content-type:text/html\n"

import random
import cgi
import cgitb
import data
cgitb.enable()





def quiz(question, answer, wrong1, wrong2, wrong3):
    """will accept a question and 4 answer choices in string format, and
    will format this into a quiz"""
    s = question
    s += '<br><form action="check.py" method="GET"><br>'
    """Organizes the 4 answer choices completely randomly"""
    if random.randrange(4) == 0:
        s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
        if random.randrange(3) == 0:
            s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            else:
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
        elif random.randrange(3) == 1:
            s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            else:
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
        else:
            s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
            else:
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
    elif random.randrange(4) == 1:
        s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
        if random.randrange(3) == 0:
            s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            else:
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
        elif random.randrange(3) == 1:
            s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            else:
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
                s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
        else:
            s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
                s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
            else:
                s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
    elif random.randrange(4) == 2:
        s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
        if random.randrange(3) == 0:
            s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            else:
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
                s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
        elif random.randrange(3) == 1:
            s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            else:
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
        else:
            s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
            else:
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
                s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
    else:
        s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
        if random.randrange(3) == 0:
            s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
                s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
            else:
                s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
        elif random.randrange(3) == 1:
            s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
                s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
            else:
                s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
        else:
            s += '<input type="submit" name="' + answer +'" value="' + answer + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
            else:
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
    s += userdata
    s += '<input type="hidden" name="questionNumber" value="' + str(questionNumber) + '">'
    s += '</form>'
    return s

inputs = cgi.FieldStorage()
if 'usr' not in inputs or 'password' not in inputs:
    print '<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body><center><a href=index.html>Userdata Not Found</a></center></body></html>'
else:
    print data.header
    usr = inputs['usr'].value
    password = inputs['password'].value
    d = data.namedict()
    level = d[usr][1]
    if level == '0':
        print '<h1>You have been blocked from the site.</h1><br><a href=index.html>Click to go back to Login</a>'
    else:
        userdata = "<input type='hidden' name='usr' value='" + usr + "'><input type='hidden' name='password' value=" + password + "><input type='hidden' name='level' value='" + level + "'>"
        print '<html><body>You cannot pass!</title> Hello ' + usr + '!<br>If you use Google, <b> WE WILL FIND OUT! YOU CAN KEEP NO SECRETS FROM US, ' + usr + '!<br></b>'
        """File in format 'question%@answer%@wrong1%@wrong2%@wrong3\nquestion%@..."""
        f = open('nerd.txt')
        s = f.read()
        f.close()
        s = s.split('\n')
        questionNumber = random.randrange(len(s))
        s = s[questionNumber]
        s = s.split('%@')
        print quiz(s[0], s[1], s[2], s[3], s[4])

print data.footer
