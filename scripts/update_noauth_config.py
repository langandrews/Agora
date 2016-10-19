import sys

# This should be ['update_noauth_config.py', 'Port', 'num'], num is the port of the entry
# we want to remove from /etc/guacamole/noauth-config.xml
args = str(sys.argv)
print args

content = [line.rstrip('\n') for line in open('/etc/guacamole/noauth-config.xml')]
i = 1
for line in content:
  print str(i) + line
  i += 1
  if args[2] in line:
    print "Line " + str(i) + "has the port"
