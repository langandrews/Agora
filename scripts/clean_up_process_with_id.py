import sys

# This program should be run like:
# python2 clean_up_process_with_id.py $id
args = sys.argv
id = '-' + args[1] + '-'

# Get all connections from noauth-config.xml
file = open('/etc/guacamole/noauth-config.xml', 'r')
lines = file.read().split('\n')
port = ""
for i in range(len(lines)):
  if id in lines[i]:
    # Get the port that we had used
    port = str(int(lines[i+2].split("'")[3]) - 5900)
    # We don't want to keep the lines that relate to this process
    del lines[i:i+4]
    break

# Clean up the noauth-config
file = open('/etc/guacamole/noauth-config.xml', 'w')
del lines[-1]
for line in lines:
  file.write(line + "\n");
file.close()

# Remove this port from current_ports.txt
print port
file = open('/home/Agora/resources/current_ports.txt', 'r')
lines = file.readlines()
file.close()
file = open('/home/Agora/resources/current_ports.txt', 'w')
for line in lines:
  if line != port+"\n":
    print line
    file.write(line)
file.close()
