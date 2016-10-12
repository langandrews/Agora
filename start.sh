#!/bin/bash
#
# Agora
# Authors: Drew Campo and Corwin Webster
# Expanded by: Joel Stehouwer and Andrew Lang
############

# Log file that this script writes to
logfile="/home/Agora/logs/start_sh.log"
echo -e "Start begin" >> $logfile

############
# Find the next available port from port.txt, then increment port number
filename="/home/Agora/port.txt"
# TODO lock the file first
nextPort=`cat $filename`
if [ "$nextPort" -gt 5999 ]
  then  nextPort="5901" 
fi
echo $((nextPort+1)) > $filename
# TODO unlock the file
nextDisplay=$((nextPort-5900))
echo "Read $nextPort from file"
echo "Display will be $nextDisplay"
echo -e "Next display is $nextDisplay" >> $logfile

############
# Grab the python program dynamically from the command line. 
# However, this program name could be different from the path. Need a way to connect them.
progName=$1
langVersion=$2
echo "Language is $langVersion"
echo -e "Program Name: $progName, and Language Version $langVersion" >> $logfile

############
# Start the display, Xvfb, python program, and x11vnc
export DISPLAY=:$nextDisplay
echo "AGORA:Display $nextDisplay set..."

/usr/bin/Xvfb :$nextDisplay -screen 0 1366x766x24 &
# Save the pid this xvfb is started on, keep a file for the most recent one
thisPid=$!
touch /home/Agora/pids/${thisPid}.pid
echo $thisPid > /home/Agora/pids/$thisPid.pid
echo $thisPid > /home/Agora/pids/recent.txt
echo "AGORA:Xvfb starting on $nextDisplay ..."
echo -e "Agora process for $progName on pid $thisPid" >> $logfile
echo -e "Agora:Xvfb starting on $nextDisplay" >> $logfile

# Handle different python versions
if [ "$langVersion" = "p2" ]
  then
    python /home/Agora/python/$progName &
    echo "python 2"
    echo -e "$progName python 2 running" >> $logfile

  elif [ "$langVersion" = "p3" ]
  then
    python3 /home/Agora/python/$progName &
    echo "python 3"
    echo -e "$progName python 3 running" >> $logfile
  elif [ "$langVersion" = "j" ]
  then
    java /home/Agora/java/$progName &
    echo "java"
    echo -e "$progName java running" >> $logFile
fi
#python3 /home/Agora/python/108/108-final-examples/mario-cart/main.py &
echo "AGORA:starting python program $progName ..."

x11vnc -display :$nextDisplay -forever -shared -rfbport $nextPort &
echo "AGORA:x11vnc server starting on port $nextPort ..."
echo -e "Agora:x11vnc server starting on $nextPort" >> $logfile

############
# Update noauth config file with new port. Remove the last line of the file, then add the new config, then add the final closing tag again.
noauthfile="/etc/guacamole/noauth-config.xml"
sed '$ d' $noauthfile > /etc/guacamole/temp.xml
mv /etc/guacamole/temp.xml $noauthfile
echo "    <config name='${progName}-${thisPid}' protocol='vnc'>" >> $noauthfile
echo '        <param name="hostname" value="localhost" />' >> $noauthfile
echo "        <param name='port' value='$nextPort' />" >> $noauthfile
echo '    </config>' >> $noauthfile
echo '</configs>' >> $noauthfile

echo -e "Start_sh end\n\n" >> $logfile
