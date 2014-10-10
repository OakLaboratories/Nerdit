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
    s += '<br><form action="trials.py" method="GET"><br>'
    """Organizes the 4 answer choices completely randomly"""
    if random.randrange(4) == 0:
        s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
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
            s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            else:
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
        elif random.randrange(3) == 1:
            s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            else:
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
                s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
        else:
            s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
                s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
            else:
                s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
    elif random.randrange(4) == 2:
        s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
        if random.randrange(3) == 0:
            s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            else:
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
                s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
        elif random.randrange(3) == 1:
            s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            else:
                s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
        else:
            s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
            else:
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
                s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
    else:
        s += '<input type="submit" name="' + wrong3 + '" value="' + wrong3 + '">'
        if random.randrange(3) == 0:
            s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
                s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
            else:
                s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
        elif random.randrange(3) == 1:
            s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
                s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
            else:
                s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
        else:
            s += '<input type="submit" name="' + answer + '" value="' + answer + '">'
            if random.randrange(2) == 0:
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
            else:
                s += '<input type="submit" name="' + wrong1 + '" value="' + wrong1 + '">'
                s += '<input type="submit" name="' + wrong2 + '" value="' + wrong2 + '">'
    s += userdata
    s += '<input type="hidden" name="qnumber" value="' + str(int(qnumber) + 1) + '">'
    s += '<input type="hidden" name="questionNumber" value="' + str(questionNumber) + '">'
    s += '</form>'
    return s

inputs = cgi.FieldStorage()
if 'usr' not in inputs or 'password' not in inputs or 'level' not in inputs:
    print '<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body><center><a href=index.html>Userdata Not Found</a></center></body></html>'
else:
    print data.header
    level = inputs['level'].value
    if level == '0':
        print '<h1>You have been blocked from the site.</h1><br><a href=index.html>Click to go back to Login</a>'
    else:
        questionNumber = inputs['questionNumber'].value
        qnumber = inputs['qnumber'].value
        usr = inputs['usr'].value
        password = inputs['password'].value
        userdata = "<input type='hidden' name='usr' value=" + usr + "><input type='hidden' name='password' value=" + password + "><input type='hidden' name='level' value=" + level + ">"
        """File in format 'question%@answer%@wrong1%@wrong2%@wrong3\nquestion%@..."""
        f = open('nerd.txt')
        s = f.read()
        f.close()
        s = s.split('\n')
        r = s[int(questionNumber)]
        r = r.split('%@')
        if (r[2] not in inputs) and (r[3] not in inputs) and (r[4] not in inputs):
            print '<br>'
            if int(qnumber) < 5:
                questionNumber = random.randrange(len(s))
                s = s[questionNumber]
                s = s.split('%@')
                print quiz(s[0], s[1], s[2], s[3], s[4])
            elif int(qnumber) >= 5:
                lst = data.subsplit('names.txt', '@%')
                count = 0
                while count < len(lst):
                    if lst[count][0] == usr:
                        if lst[count][2] == '5':
                            print "<h1>You are already on the admin level!</h1>"
                        elif int(lst[count][2]) < 4:
                            lst[count][2] = str(int(lst[count][2]) + 1)
                            level = lst[count][2]
                            userdata = "<input type='hidden' name='usr' value=" + usr + "><input type='hidden' name='password' value=" + password + "><input type='hidden' name='level' value=" + level + ">"
                            f = open('names.txt', 'w')
                            ncount = 0
                            print 'Your level has been increased to ' + str(int(lst[count][2])) + '!<br>'
                            
                            while (ncount < len(lst)):
                                f.write(lst[ncount][0] + '@%' + lst[ncount][1] + '@%' + lst[ncount][2] + '\n')
                                ncount += 1
                        elif int(lst[count][2]) == 4:
                            print "<h1>You are on the highest level. To be increase to the even higher level, you must enter the admin password below!</h1>"
                    count += 1
        else:
            print '<h1>You are incorrect!</h1>'
            print '<form action="trials.py" method="GET">' + userdata + '<input type="hidden" name="qnumber" value="0"><input type="hidden" name="questionNumber" value="0"><input type="submit" name="quiz" value="Try again"></form>'
        print "<br><form action='home.py' method='GET'>" + userdata
        print "<input type='submit' class='linkbutton' name='home' value='Click to Return to Homepage'></form>"
        print '<br><br><form action="admin.py" type="GET">' + userdata + '<input type="password" name="adminpw" required><input type="submit" name="admin" value="Upgrade to Admin"></form>'
        print data.footer


