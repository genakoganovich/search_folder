import os
os.chdir('//192.168.20.235/d$/data/_FTP Incoming/Israel Projects/_Priority_Lines/_RecentVersion/')
done = '//192.168.20.235/d$/data/_FTP Incoming/Israel Projects/_Priority_Lines/_RecentVersion/001_done_lines.txt'
start = ('ds', 'em', 'gi', 'mi', 'vs', 'ar', 'lp', 'rv')

lines = set()
with open(done, 'r') as f_in:
    done_lines = [str(item).strip() for item in f_in.readlines()]

for root, dirs, files in os.walk(".", topdown=False):
    for name in [item for item in dirs if item.startswith(start)]:
        if name not in done_lines:
            lines.add(name)

with open('todo_lines.txt', 'w') as f_out:
    for line in lines:
        f_out.write(line + '\n')
        print(line)
