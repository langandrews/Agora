#!/bin/bash
# Script to build the maven project then copy the resulting war file to the webapps directory.

mvn package
cd target
# I don't know if we need the war file or if we need the target folder stuff...  Maybe we only want the war file?
mv agoraguac-1.war agora.war
cp agora.war /home/Agora/webapps
rm -r agora.war
rm -r agora
mv agoraguac-1 agora
cp -r agora /home/Agora/webapps
echo "agora app deployed"

# Restart required services
service guacd restart
service tomcat7 restart
echo "guacd and tomcat7 restarted"
