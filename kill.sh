#!/bin/bash
#
#
# Should we do this in python instead??
#################

logfile="/home/Agora/logs/kill_sh.log"

# Kill the process specified by command line arg
pid=$1
kill ${pid}
echo "kill.sh: Killing process ${pid}"

echo -e "Killing pid $pid" >> $logfile

# Should also edit noauth-config to get rid of the corresponding entry
