#!/bin/bash
#
# Agora
# Authors: Drew Campo and Corwin Webster
############

############
# Find the next available port from port.txt, then increment port number
filename="/home/AgoraGuac/port.txt"
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

############
# Grab the python program dynamically from the command line. 
# However, this program name could be different from the path. Need a way to connect them.
progName=$1
pyVersion=$2
echo "python version is $pyVersion"

############
# Start the display, Xvfb, python program, and x11vnc
export DISPLAY=:$nextDisplay
echo "AGORA:Display $nextDisplay set..."

/usr/bin/Xvfb :$nextDisplay -screen 0 1366x766x24 &
# Save the pid this xvfb is started on, keep a file for the most recent one
thisPid=$!
touch /home/AgoraGuac/pids/${thisPid}.pid
echo $thisPid > /home/AgoraGuac/pids/${thisPid}.pid
echo $thisPid > /home/AgoraGuac/pids/recent.txt
echo "AGORA:Xvfb starting on $nextDisplay ..."

# Handle different python versions
if [ "$pyVersion" = 2 ]
  then
    python /home/AgoraGuac/python/$progName &
    echo "python 2"
  else
    python3 /home/AgoraGuac/python/$progName &
    echo "python 3"
fi
#python3 /home/AgoraGuac/python/108/108-final-examples/mario-cart/main.py &
echo "AGORA:starting python program $progName ..."

x11vnc -display :$nextDisplay -forever -shared -rfbport $nextPort &
echo "AGORA:x11vnc server starting on port $nextPort ..."

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
