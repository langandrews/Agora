import sys

file = open('/home/Agora/resources/current_ports.txt', 'r+')
current_ports = file.read().split('\n')
port = 0
for i in range(1,100):
  if not (str(i) in current_ports):
    file.write(str(i) + "\n")
    port = i
    break

file.close()
sys.exit(port)
