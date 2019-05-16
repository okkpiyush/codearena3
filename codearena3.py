s = "aahkcrehaccccccckkkkkerearthhhackerearttheatrha"
l = len(s)
code = [0,0,0,0,0,0,0]
count=0
for i in range(0,l):
    if s[i] == 'h':
        code[0] = code[0] + 1
    elif s[i] == 'a':
        code[1] = code[1] + 1
    elif s[i] == 'c':
        code[2] = code[2] + 1
    elif s[i] == 'k':
        code[3] = code[3] + 1
    elif s[i] == 'e':
        code[4] = code[4] + 1
    elif s[i] == 'r':
        code[5] = code[5] + 1
    elif s[i] == 't':
        code[6] = code[6] + 1

new = list()
new.append(code[2])
new.append(code[3])
new.append(code[6])
print(min(new))