def change(s):
    while True:
            count = s.count('.')
            for i in range(2, s.count('.')+1):
                s = s.replace('.'*i, '.')
            if count == s.count('.'):
                break
    return s

def change2(s):
    for _ in range(2):
            if len(s) >= 2:
                if s[0] == '.':
                    s = s[1:]
                elif s[-1] == '.':
                    s = s[:-1]
            else:
                if s[0:] == '.':
                    s = ''
    return s

def solution(id):
    answer = ''
    if id:
        id = id.lower()
        new = ''
        for s in id:
            if 97 <= ord(s) <= 122:
                new += s
            elif s == '-' or s == '.' or s == '_':
                new += s
            elif s.isdigit():
                new += s
                
        new = change(new)
        new = change2(new)
        if new == '':
            new = 'aaa'
        if len(new) >= 16:
            new = new[:15]
            new = change2(new)
        elif 0 <len(new) <= 2:
            new = change2(new)
            new = new + new[-1]*(3 - len(new))
    else:
        new = 'aaa'
    return new

# 다른사람 풀이
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
