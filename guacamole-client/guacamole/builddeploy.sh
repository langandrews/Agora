#!/bin/bash
# Script to build the maven project then copy the resulting war file to the webapps directory.

mvn package
cd target
mv agoraguac-1.war agoraguac.war
cp agoraguac.war /var/lib/tomcat7/webapps
echo "agoraguac app deployed"
