#!/bin/bash
# Script to install the full Agora system.

here=$(pwd)
logFile=$(pwd)"/install_log.txt"

echo -e "Installing Agora to your machine.  Please be patient as we install a lot of dependencies...\nIf there are any errors, please refer to $logFile" 2>&1


# Install dependencies
echo -e "Installing dependencies (expect this to take a long time)"
apt-get install -y make libcairo2-dev libpng12-dev libjpeg-dev libossp-uuid-dev  freerdp-x11 libssh2-1 libfreerdp-dev libvorbis-dev gcc libssh-dev libpulse-dev tomcat7 tomcat7-admin tomcat7-docs libpango1.0-dev libssh2-1-dev git python-tk > $logFile 2>&1
echo -e "Wave 1 installed"
apt-get install -y libvncserver-dev > $logFile 2>&1
echo -e "Wave 2 installed"
apt-get install -y xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic x11-apps x11vnc > $logFile 2>&1
echo -e "Wave 3 installed"
apt-get install -y maven > $logFile 2>&1
echo -e "Wave 4 installed"
apt-get install -y default-jdk > $logFile 2>&1
echo -e "Wave 5 installed"
echo -e "Finished installing dependencies\n"


# Download and install guacamole.
echo -e "Download and install guacamole"
wget -O guacamole-server-0.9.9.tar.gz http://sourceforge.net/projects/guacamole/files/current/source/guacamole-server-0.9.9.tar.gz/download > $logFile 2>&1
tar -xvzf guacamole-server-0.9.9.tar.gz > $logFile 2>&1
cd guacamole-server-0.9.9 > $logFile 2>&1
./configure --with-init-dir=/etc/init.d > $logFile 2>&1
make && make install > $logFile 2>&1
update-rc.d guacd defaults > $logFile 2>&1
ldconfig > $logFile 2>&1
mkdir /etc/guacamole > $logFile 2>&1
cd /home/Agora > $logFile 2>&1
rm -r $here/guacamole-server-0.9.9/ > $logFile 2>&1
rm $here/guacamole-server-0.9.9.tar.gz $logFile 2>&1
echo -e "Finished installing guacamole\n"


# Clone Agora repo to /home folder.
echo -e "Get Agora from github"
cd /home > $logFile 2>&1
git clone https://github.com/solsaver/Agora > $logFile 2>&1
echo -e "Finished configuring Agora\n"


# Install guacamole-auth-noauth extension.
echo -e "Install guacamole no-auth extension"
wget -O guacamole-auth-noauth-0.9.8.tar.gz https://sourceforge.net/projects/guacamole/files/current/extensions/guacamole-auth-noauth-0.9.8.tar.gz/download > $logFile 2>&1
tar -xvzf guacamole-auth-noauth-0.9.8.tar.gz > $logFile 2>&1
mkdir /etc/guacamole/extensions > $logFile 2>&1
cp guacamole-auth-noauth-0.9.8/guacamole-auth-noauth-0.9.8.jar /etc/guacamole/extensions > $logFile 2>&1
rm guacamole-auth-noauth-0.9.8.tar.gz > $logFile 2>&1
rm -r guacamole-auth-noauth-0.9.8 > $logFile 2>&1
echo -e "Finished installing guacamole no-auth extension\n"


# Copy over guacamole setting files.
echo -e "Configure guacamole settings"
cp Agora/settings-guac/* /etc/guacamole > $logFile 2>&1
cd /etc/guacamole > $logFile 2>&1
chmod 777 . > $logFile 2>&1
echo -e "Finished configuring guacamole settings\n"


# Make a link to the properties file so that the guacaole server can read it.
echo -e "Set up tomcat7"
mkdir /usr/share/tomcat7/.guacamole > $logFile 2>&1
ln -s /etc/guacamole/guacamole.properties /usr/share/tomcat7/.guacamole > $logFile 2>&1

# make a link to the webapps files to override tomcat's default page with the Agora page.
rm -r /var/lib/tomcat7/webapps > $logFile 2>&1
ln -s /home/Agora/webapps /var/lib/tomcat7/ > $logFile 2>&1
echo -e "Finished setting up tomcat7\n"


# Build the maven project then copy the resulting war file to the webapps directory.
echo -e "Build the maven project"
cd /home/Agora/guacamole-client/guacamole > $logFile 2>&1
mvn package > $logFile 2>&1
cd target > $logFile 2>&1
mv agoraguac-1.war agoraguac.war > $logFile 2>&1
cp agoraguac.war /home/Agora/webapps > $logFile 2>&1
echo -e "Finished building the maven project\n"


echo -e "Set up permissions and create neccessary folders and files"
cd /home/Agora > $logFile 2>&1
sudo chmod 666 pids
touch pids/recent.txt
sudo chmod 666 pids/recent.txt
mkdir /home/Agora/logs
sudo chmod 777 /home/Agora/logs
touch /home/Agora/logs/start_sh.log
sudo chmod 777 /home/Agora/logs/start_sh.log
echo -e "Finished setting up permissions\n"

# Start/Restart required services
echo -e "Restart guacd and tomcat7"
service guacd start > $logFile 2>&1
service tomcat7 restart > $logFile 2>&1
echo -e "Agora has been deployed, navigate to localhost:8080 to see the results"
