#!/bin/bash
# Script to build the maven project then copy the resulting war file to the webapps directory.

mvn package
cd target
# I don't know if we need the war file or if we need the target folder stuff...  Maybe we only want the war file?
mv agoraguac-1.war agoraguac.war
cp agoraguac.war /home/Agora/webapps
mv agoraguac-1 agoraguac
cp -r agoraguac /home/Agora/webapps
echo "agoraguac app deployed"

# Restart required services
service guacd restart
service tomcat7 restart
echo "guacd and tomcat7 restarted"
