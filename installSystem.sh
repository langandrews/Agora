#!/bin/bash
# Script to install the full Agora system.

logFile=$(pwd)"/install_log.txt"

echo -e "Installing Agora to your machine.  Please be patient as we install a lot of dependencies...\nIf there are any errors, please refer to $logFile"


# Install dependencies
echo -e "Installing dependencies (expect this to take a long time)"
apt-get install -y make libcairo2-dev libpng12-dev libjpeg-dev libossp-uuid-dev  freerdp-x11 libssh2-1 libfreerdp-dev libvorbis-dev gcc libssh-dev libpulse-dev tomcat7 tomcat7-admin tomcat7-docs libpango1.0-dev libssh2-1-dev git python-tk >> $logFile
echo -e "Wave 1 installed"
apt-get install -y libvncserver-dev >> $logFile
echo -e "Wave 2 installed"
apt-get install -y xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic x11-apps x11vnc >> $logFile
echo -e "Wave 3 installed"
apt-get install -y maven >> $logFile
echo -e "Wave 4 installed"
apt-get install -y default-jdk >> $logFile
echo -e "Wave 5 installed"
echo -e "Finished installing dependencies\n"


# Download and install guacamole.
echo -e "Download and install guacamole"
wget -O guacamole-server-0.9.9.tar.gz http://sourceforge.net/projects/guacamole/files/current/source/guacamole-server-0.9.9.tar.gz/download >> $logFile
tar -xvzf guacamole-server-0.9.9.tar.gz >> $logFile
cd guacamole-server-0.9.9 >> $logFile
./configure --with-init-dir=/etc/init.d >> $logFile
make && make install >> $logFile
update-rc.d guacd defaults >> $logFile
ldconfig >> $logFile
mkdir /etc/guacamole >> $logFile
cd /home/Agora >> $logFile
rm -r guacamole-server-0.9.9/ >> $logFile
rm guacamole-server-0.9.9.tar.gz $logFile
echo -e "Finished installing guacamole\n"


# Clone Agora repo to /home folder.
echo -e "Get Agora from github"
cd /home >> $logFile
git clone https://github.com/solsaver/Agora >> $logFile
echo -e "Finished configuring Agora\n"


# Install guacamole-auth-noauth extension.
echo -e "Install guacamole no-auth extension"
wget -O guacamole-auth-noauth-0.9.8.tar.gz https://sourceforge.net/projects/guacamole/files/current/extensions/guacamole-auth-noauth-0.9.8.tar.gz/download >> $logFile
tar -xvzf guacamole-auth-noauth-0.9.8.tar.gz >> $logFile
mkdir /etc/guacamole/extensions >> $logFile
cp guacamole-auth-noauth-0.9.8/guacamole-auth-noauth-0.9.8.jar /etc/guacamole/extensions >> $logFile
rm guacamole-auth-noauth-0.9.8.tar.gz >> $logFile
rm -r guacamole-auth-noauth-0.9.8 >> $logFile
echo -e "Finished installing guacamole no-auth extension\n"


# Copy over guacamole setting files.
echo -e "Configure guacamole settings"
cp Agora/settings-guac/* /etc/guacamole >> $logFile
cd /etc/guacamole >> $logFile
chmod 777 . >> $logFile
echo -e "Finished configuring guacamole settings\n"


# Make a link to the properties file so that the guacaole server can read it.
echo -e "Set up tomcat7"
mkdir /usr/share/tomcat7/.guacamole >> $logFile
ln -s /etc/guacamole/guacamole.properties /usr/share/tomcat7/.guacamole >> $logFile

# make a link to the webapps files to override tomcat's default page with the Agora page.
rm -r /var/lib/tomcat7/webapps >> $logFile
ln -s /home/Agora/webapps /var/lib/tomcat7/ >> $logFile
echo -e "Finished setting up tomcat7\n"


# Build the maven project then copy the resulting war file to the webapps directory.
echo -e "Build the maven project"
cd /home/Agora/guacamole-client/guacamole >> $logFile
mvn package >> $logFile
cd target >> $logFile
mv agoraguac-1.war agoraguac.war >> $logFile
cp agoraguac.war /home/Agora/webapps >> $logFile
echo -e "Finished building the maven project\n"


# Start/Restart required services
echo -e "Restart guacd and tomcat7"
service guacd start >> $logFile
service tomcat7 restart >> $logFile
echo -e "Agora has been deployed, navigate to localhost:8080 to see the results"
