#!/bin/bash
# Script to install the full Agora system.

# Gain root access. This is necessary to install Agora.
sudo su

# Install dependencies
apt-get install -y make libcairo2-dev libpng12-dev libjpeg62-dev libossp-uuid-dev  freerdp-x11 libssh2-1 libfreerdp-dev libvorbis-dev libssl0.9.8 gcc libssh-dev libpulse-dev tomcat7 tomcat7-admin tomcat7-docs libpango1.0-dev libssh2-1-dev git python-tk libvncserver-dev xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic x11-apps x11vnc maven default-jdk

# Download and install guacamole.
wget -O guacamole-server-0.9.9.tar.gz http://sourceforge.net/projects/guacamole/files/current/source/guacamole-server-0.9.9.tar.gz/download
tar -xvzf guacamole-server-0.9.9.tar.gz
cd guacamole-server-0.9.9
./configure --with-init-dir=/etc/init.d
make && make install
update-rc.d guacd defaults
ldconfig
mkdir /etc/guacamole

# Clone Agora repo to /home folder.
cd /home
git clone https://github.com/solsaver/Agora

# Install guacamole-auth-noauth extension.
wget -O guacamole-auth-noauth-0.9.8.tar.gz https://sourceforge.net/projects/guacamole/files/current/extensions/guacamole-auth-noauth-0.9.8.tar.gz/download
tar -xvzf guacamole-auth-noauth-0.9.8.tar.gz
mkdir /etc/guacamole/extensions
cp guacamole-auth-noauth-0.9.8/guacamole-auth-noauth-0.9.8.jar /etc/guacamole/extensions
rm guacamole-auth-noauth-0.9.8.tar.gz
rm -r guacamole-auth-noauth-0.9.8

# Copy over guacamole setting files.
cp Agora/settings-guac/* /etc/guacamole
cd /etc/guacamole
chmod 777 .

# Make a link to the properties file so that the guacaole server can read it.
mkdir /usr/share/tomcat7/.guacamole
ln -s /etc/guacamole/guacamole.properties /usr/share/tomcat7/.guacamole

# make a link to the webapps files to override tomcat's default page with the Agora page.
ln -s /home/Agora/webapps /var/lib/tomcat7/webapps

# Build the maven project then copy the resulting war file to the webapps directory.
cd /home/Agora/guacamole-client/guacamole
mvn package
cd target
mv agoraguac-1.war agoraguac.war
cp agoraguac.war /home/Agora/webapps
echo "agoraguac app deployed"

# Start/Restart required services
service guacd start
service tomcat7 restart


