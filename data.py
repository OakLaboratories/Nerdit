import cgi
import datetime

def namedict():
    """Takes the names.txt file and sorts it into a dictionary with the name as a key, attached to a list of the password and level"""
    f = open('names.txt')
    s = f.read()
    f.close()
    lst = s.split('\n')
    count = 0
    d = {}
    while count < len(lst):
        newl = lst[count].split('@%')
        if len(newl) == 3:
            d[newl[0]] = newl[1:]
        count += 1
    return d

def timenow():
    """Returns the date and time in a formatted string"""
    t = datetime.datetime.now()
    dts = str(t.month) + '/' + str(t.day) + '/' + str(t.year) + ', '
    if t.hour > 12:
        dts = dts + str((t.hour - 12)) + ':'
    else:
        dts = dts + str(t.hour) + ':'
    if t.minute < 10:
        dts = dts + '0' + str(t.minute)
    else:
        dts = dts + str(t.minute)
    if t.hour > 12:
        dts += " PM"
    else:
        dts += " AM"
    return dts

def subsplit(f, x):
    """Takes a file with multiple lines and dividers in each line, splits it by line, and then splits each line into a sublist by the divider"""
    f = open(f)
    s = f.read()
    f.close()
    lst = s.split('\n')
    lst = lst[:len(lst)-1]
    count = 0
    while count < len(lst):
        ilist = lst[count].split(x)
        lst[count] = ilist
        count += 1
    return lst

def countLike(n):
    """Count the number of likes on page n"""
    lst = subsplit('like.txt', '&')
    count = 0
    total = 0
    while count < len(lst):
        if lst[count][1] == n:
            total += int(lst[count][2])
        count += 1
    return total

def check(s):
    """Checks for certain characters to remove"""
    count = 0
    while count < len(lst):
        if lst[count] in s:
            x = s.find(lst[count])
            s = s[:x] + s[x+len(lst[count]):]
        else:
            count += 1
    return s

def numbercheck(s):
    """Checks for numbers to remove"""
    count = 0
    while count < len(s):
        if ord(s[count]) >= ord('0') and ord(s[count]) <= ord('9'):
            s = s[:count] + s[count + 1:]
        else:
            count += 1
    return s

def htmlcheck(s):
    """Checks for characters to convert into HTML format"""
    count = 0
    lst = d.keys()
    while count < len(lst):
        if lst[count] in s:
            x = s.find(lst[count])
            s = s[:x] + d[lst[count]] + s[x+len(lst[count]):]
        else:
            count += 1
    return s

lst = [',', '\n', '@', '%', '<', '>', '&']
d = {"'":'&#39;', '"':'&quot;', '\\':'&#92;'}
header = '<!DOCTYPE html><html><head><title>Nerdit</title><link rel="stylesheet" type="text/css" href="nerdit.css"></head><body>'
footer = '</body></html>'
