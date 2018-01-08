#RUN LENGTH COMPRESSION ALGORITHM

def compress(s):
    r = ''
    l = len(s)

    #Edge case

    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s + "1"

    i = 1
    cnt = 1

    while i < l:
        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1
        i += 1
    r = r + s[i-1] + str(cnt)
    print r
