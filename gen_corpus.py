f1 = open("bopomo-aishell.txt").readlines()
d1 = {}
for i in range(len(f1)):
    line = f1[i].strip().split(' ')
    d1[line[0]] = ' '.join(line[1:])

f2 = open("trad-aishell.txt").readlines()
d2 = {}
for i in range(len(f2)):
    line = f2[i].strip().split(' ')
    d2[line[0]] = ''.join(line[1:])

ret = []
for k in d1:
    bpm = d1[k].split(' ')
    trd = list(d2[k])
    if len(bpm) != len(trd):
        print(bpm, trd)
        continue
    tmp = ""
    for i, j in zip(bpm, trd):
        tmp += j + ":" + i + ' '
    ret.append(tmp[:-1])

fw = open('data-aishell.txt', 'w')
fw.writelines([(x+'\n') for x in ret])