#!/usr/bin/python
print 'Content-type:text/html\n'

import cgi
import cgitb
import datetime
import data
cgitb.enable()

def pageform(usr):
    """Shows the form to create a new page"""
    print data.header
    print '<center>'
    print '<h1>Create New Thread</h1>'
    print '<form action="pageform2.py" method="POST" id="new">'
    print 'Thread Name (Note - Commas will not appear in title):'
    print '<input type="text" name="name" required><br>Post:'
    print '<br><textarea name="newpost" id="new" required></textarea><br>'
    print userdata
    print '<input type="submit" name="create" value="Submit"></form></center>'
    print data.footer

def newpage(name, newpost, usr):
    """Creates a new page in the pages.txt file"""
    name = data.check(name)
    newpost = data.check(newpost)
    f = open('posts.txt')
    s = f.read()
    f.close()
    lst = s.split('\n')
    lst = lst[:len(lst)-1]
    if len(lst) == 0:
        pagename = '1'
    else:
        newl = lst[len(lst)-1].split('@%')
        pagename = str(int(newl[1]) + 1)
    dts = data.timenow()
    f = open('posts.txt', 'a')
    f.write(name + '@%' + pagename + '@%' + usr + '@%' + newpost + "@%" + dts + '\n')
    f.close()
    print data.header
    print "Your page has been created. Click <form class='inform' action='pageform2.py' method='POST'><input type='hidden' name='n' value=" + pagename + ">" + userdata
    print "<input type='submit' class='linkbutton' name='display' value='Here'></form> to visit the page."
    print data.footer
    
def displaypage(n, usr, level):
    """Displays the page with the code n"""
    print data.header
    f = open('posts.txt')
    s = f.read()
    f.close()
    lst = s.split('\n')
    newl = lst[int(n)-1].split('@%')
    print '<h1>' + newl[0] + '</h1><h3>By ' + newl[2] + '</h3><p>' + newl[3] + '</p>'
    print 'Likes: ' + str(data.countLike(n))
    
    print '<form action="pageform2.py" method="POST">' + userdata
    print "<input type='hidden' name='n' value=" + n + "><input type='submit' name='like' class='linkbutton' value='Like Page'> or <input type='submit' name='dislike' class='linkbutton' value='Dislike Page'></form><br>"
    print "Comments:<br>" + showComments(usr, n)
    print "<br>Write Comment: <form action='pageform2.py' method='POST' id='reply'><textarea form='reply' name='comment'></textarea><input type='hidden' name='parent' value='0'><input type='hidden' name='cid' value=" + newId(n, '0') + ">"
    print "<br>" + userdata + "<input type='hidden' name='n' value=" + n + "><input type='submit' name='write' value='Post Comment'></form>"
    if newl[2] == usr or level == '5':
        print "<br><form action='pageform2.py' method='POST'>" + userdata + "<input type='hidden' name='n' value=" + n + "><input type='submit' name='delete' value='Delete Page' class='linkbutton'></form>"
    print "<br><br><form action='home.py' method='POST'>" + userdata + '<input type="submit" name="home" value="Return to homepage" class="linkbutton"></form>' 
    print data.footer

def likePage(n, usr, tlike):
    """Adds a like/dislike to a page, or changes it if done already oppositely"""
    lst = data.subsplit('like.txt', '&')
    print data.header
    count = 0
    total = 0
    while count < len(lst):
        if lst[count][0] == usr and lst[count][1] == n:
            total += int(lst[count][2])
        count += 1
    if total == tlike :
        if tlike == -1:
            print '<h1>Page cannot be disliked again</h1>'
        else:
            print '<h1>Page cannot be liked again</h1>'
    else:
        f = open('like.txt', 'a')
        f.write(usr + '&' + n + '&' + str(tlike - total) + '\n')
        f.close()
        if tlike == -1:
            print '<h1>Page has been disliked</h1>'
        else:
            print '<h1>Page has been liked</h1>'
    print "<form action='pageform2.py' method='POST'>" + userdata
    print "<input type='hidden' name='n' value=" + n + "><input type='submit' name='display' value='Click to go back' class='linkbutton'></form>"
    print data.footer

def showComments(usr, n):
    """Prints comments"""
    lst = data.subsplit('comments.txt', '@%')
    comments = lookGive(usr, lst, '0', n)
    return comments

def lookGive(usr, lst, parent, n):
    """Returns a string with comments and subcomments put into a list in order of time written"""
    comments = "<ul>"
    count = 0
    while count < len(lst):
        if lst[count][1] == n and lst[count][4] == parent:
            comments += "<li>" + lst[count][0] + ", " + lst[count][3] + ' - ' + lst[count][2] + " "
            comments += "<form style='display:inline;' action='pageform2.py' method='POST'><input type='hidden' name='parent' value=""" + lst[count][4] + ">"
            comments += userdata
            comments += "<input type='hidden' name='n' value=" + n + ">"
            comments += "<input type='hidden' name='cid' value=" + lst[count][5] + " ><input type='submit' name='reply' value='Reply' class='linkbutton'></form>"
            newParent = lst[count][4] + '-' + lst[count][5]
            comments += lookGive(usr, lst, newParent, n)
            comments += "</li>"
        count += 1
    comments += "</ul>"
    return comments

def writeComment(usr, n, comment, parent, cid):
    """Writes a comment, adding it to the comment.txt file"""
    comment = data.check(comment)
    f = open('comments.txt', 'a')
    dts = data.timenow()
    f.write(usr + '@%' + n + '@%' + comment + '@%' + dts + '@%' + parent + '@%' + cid + '\n')
    f.close()
    print data.header
    print "<h1>Comment has been posted</h1>"
    print "<form action='pageform2.py' method='POST'>" + userdata
    print "<input type='hidden' name='n' value=" + n + "><input type='submit' name='display' value='Click to go back' class='linkbutton'></form>"
    print data.footer

def delete(usr, n):
    """Deletes a post and all data having to do with the page from the site"""
    plst = data.subsplit('posts.txt', '@%')
    clst = data.subsplit('comments.txt', '@%')
    llst = data.subsplit('like.txt', '&')
    print data.header
    if plst[int(n)-1][2] != usr and (int(level) < 5):
        print "<h1>You do not have permission to delete this.</h1>"
    else:
        plst.pop(int(n)-1)
        p = ""
        c = ""
        l = ""
        count = int(n) - 1
        while count < len(plst):
            plst[count][1] = str(int(plst[count][1]) - 1)
            count += 1
        count = 0
        while count < len(plst):
            icount = 0
            while icount < len(plst[count]):
                p += plst[count][icount]
                p += "@%"
                icount += 1
            p = p[:len(p)-2]
            p += '\n'
            count += 1
        count = 0
        while count < len(clst):
            if clst[count][1] == n:
                clst.pop(count)
            count += 1
        count = 0
        while count < len(clst):
            if int(clst[count][1]) > int(n):
                clst[count][1] = str(int(clst[count][1]) - 1)
            count += 1
        count = 0
        while count < len(clst):
            icount = 0
            while icount < len(clst[count]):
                c += clst[count][icount]
                c += "@%"
                icount += 1
            c = c[:len(c)-2]
            c += '\n'
            count += 1
        count = 0
        while count < len(llst):
            if llst[count][1] == n:
                llst.pop(count)
            count += 1
        count = 0
        while count < len(llst):
            if int(llst[count][1]) > int(n):
                llst[count][1] = str(int(llst[count][1]) - 1)
            count += 1
        count = 0
        while count < len(llst):
            icount = 0
            while icount < len(llst[count]):
                l += llst[count][icount]
                l += "&"
                icount += 1
            l = l[:len(l)-1]
            l += '\n'
            count += 1
        pfile = open('posts.txt', 'w')
        pfile.write(p)
        pfile.close()
        cfile = open('comments.txt', 'w')
        cfile.write(c)
        cfile.close()
        lfile = open('like.txt', 'w')
        lfile.write(l)
        lfile.close()
        print "<h1>Post deleted</h1>"
    print "<br><form action='home.py' method='POST'>" + userdata
    print "<input type='submit' class='linkbutton' name='home' value='Click to return to homepage'></form>"
    print data.footer

def newId(n, parent):
    """Gives a comment its new ID number based on its parent id and the number of subcomments already present"""
    lst = data.subsplit('comments.txt', '@%')
    x = 0
    count = 0
    while count < len(lst):
        if int(lst[count][5]) > x and n == lst[count][1] and parent == lst[count][4]:
            x = int(lst[count][5])
        count += 1
    x += 1
    return str(x)

def reply(usr, n, parent, cid):
    """Prints the form to reply to a comment, and finds the parent ID"""
    parent = parent + '-' + cid
    cid = newId(n, parent)
    print data.header
    print"<h1>Reply to Comment</h1><br><form action='pageform2.py' method='POST'>Reply:<input type='text' name='comment'>"
    print userdata + "<input type='hidden' name='n' value=" + n + ">"
    print "<input type='hidden' name='parent' value=" + parent + "><input type='hidden' name='cid' value=" + cid + ">"
    print "<input type='submit' name='write' value='Write Comment' class='linkbutton'></form>"
    print data.footer

d = cgi.FieldStorage()
if 'usr' not in d or 'password' not in d or 'level' not in d:
    print '<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body><center><a href=index.html>Userdata Not Found</a></center></body></html>'
else:
    level = d['level'].value
    if level == '0':
        print '<html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body><h1>You have been blocked from the site.</h1><br><a href=index.html>Click to go back to Login</a></body></html>'
    else:
        usr = d['usr'].value
        password = d['password'].value
        userdata = "<input type='hidden' name='usr' value=" + usr + "><input type='hidden' name='password' value=" + password + "><input type='hidden' name='level' value=" + level + ">"
        permissiond = data.header + '<h1>Your nerdiness level is not high enough! Please upgrade it through the link on the homepage!</h1>'
        permissiond += '<form method="POST" action="home.py"><input type="submit" name="home" value="Return to Homepage" class="linkbutton">' + userdata + '</form>' + data.footer
        if 'make' in d:
            if int(level) >= 4:
                pageform(usr)
            else:
                print permissiond
        elif 'create' in d:
            name = d['name'].value
            newpost = d['newpost'].value
            newpage(name, newpost, usr)
        elif 'display' in d:
            n = d['n'].value
            displaypage(n, usr, level)
        elif 'like' in d:
            if int(level) >= 2:
                n = d['n'].value
                tlike = 1
                likePage(n, usr, tlike)
            else:
                print permissiond
        elif 'dislike' in d:
            if int(level) >= 2:
                n = d['n'].value
                tlike = -1
                likePage(n, usr, tlike)
            else:
                print permissiond
        elif 'write' in d:
            if int(level) >= 3:
                n = d['n'].value
                comment = d['comment'].value
                parent = d['parent'].value
                cid = d['cid'].value
                writeComment(usr, n, comment, parent, cid)
            else:
                print permissiond
        elif 'delete' in d:
            n = d['n'].value
            delete(usr, n)
        elif 'reply' in d:
            if int(level) >= 3:
                n = d['n'].value
                parent = d['parent'].value
                cid = d['cid'].value
                reply(usr, n, parent, cid)
            else:
                print permissiond


