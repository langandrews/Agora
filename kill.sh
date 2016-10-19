#!/bin/bash
#
#
# Should we do this in python instead??
#################

logfile="/home/Agora/logs/kill_sh.log"

# Kill the process specified by command line arg
pid=$1
echo "kill.sh: Killing process ${pid}"

echo -e "Killing pid $pid" >> $logfile

# Should also edit noauth-config to get rid of the corresponding entry

while IFS='' read -r line
do
  if [[ $line == *"Port"* ]]
  then
    python /home/Agora/scripts/update_noauth_config.py $line
  fi
    echo -e $line >> $logfile
    #kill $line
done < /home/Agora/pids/$pid.pid

#rm /home/Agora/pids/$pid.pid
