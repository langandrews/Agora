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

# Update the noauth-config
python ./scripts/update_noauth_config.py $pid >> $logfile

while IFS='' read -r line
do
  echo -e $pid >> $logfile
  kill $pid
done < /home/Agora/pids/$pid.pid
python2 /home/Agora/scripts/update_noauth_config.py $pid
rm /home/Agora/pids/$pid.pid
