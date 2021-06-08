#Try Regex Match
import re
import sys

#file = '/mnt/d/ebooks/deadstarrecover.txt'
file = sys.argv[1]
pattern = sys.argv[2]
with open(file, 'r') as f:
    txt = f.readlines()


prog = re.compile(pattern)
count = 0
print('Found {}'.format(pattern))
for i in txt:
    if count < 50:
        result = prog.search(i)
        if result != None:
            s, e = result.start(), result.end()
            line = result.string
            target = slice(s, e)
            rest_head = slice(0, s)
            #print(f"{rest_head=}")
            rest_tail = slice(e, len(line))
            head, target, tail = line[rest_head], line[target], line[rest_tail]
            highlight = f"{head}\033[34;40;92m{target}\033[0m{tail}"
            print(f"L{count}:{highlight}, col{s}->col{e}]")
        count += 1
    else:
        print('Done')
        break
    





