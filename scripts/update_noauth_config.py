import sys

# This program should be run like:
# python update_noauth_config.py $port $pid
args = sys.argv
pid = args[1]

file = open('noauth_config.xml', 'r')
lines = file.read().split('\n')
for i in range(len(lines)):
    if pid in lines[i]:
        del lines[i:i+4]
        break
file = open('noauth_config.xml', 'w')
for line in lines:
    file.write(line + "\n");
file.close()
