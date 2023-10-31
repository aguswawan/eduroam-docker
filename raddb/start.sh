#!/bin/bash
EDUROAM_FLR="103.220.113.18"
FLR_EDUROAM_SECRET="testing123"
YOUR_REALM1="unand.ac.id"
YOUR_REALM2="student.unand.ac.id"
LDAP_SERVER="172.17.0.3"
LDAP_IDENTITY="cn=admin,dc=example,dc=org"
LDAP_PASSWORD="bismillah"
LDAP_BASEDN="dc=example,dc=org"

chown -R freerad:freerad /etc/freeradius/3.0
sed -i -e "s/EDUROAM_FLR/$EDUROAM_FLR/g" \
       -e "s/FLR_EDUROAM_SECRET/$FLR_EDUROAM_SECRET/g" \
	   /etc/freeradius/3.0/clients-eduroam-flrs.conf

sed -i -e "s/LDAP_SERVER/$LDAP_SERVER/g" \
       -e "s/LDAP_IDENTITY/$LDAP_IDENTITY/g" \
       -e "s/LDAP_PASSWORD/$LDAP_PASSWORD/g" \
       -e "s/LDAP_BASEDN/$LDAP_BASEDN/g" \
	   /etc/freeradius/3.0/mods-enabled/ldap

sed -i -e "s/EDUROAM_FLR/$EDUROAM_FLR/g" \
       -e "s/FLR_EDUROAM_SECRET/$FLR_EDUROAM_SECRET/g" \
       -e "s/YOUR_REALM1/$YOUR_REALM1/g"  \
       -e "s/YOUR_REALM2/$YOUR_REALM2/g"  \
	   /etc/freeradius/3.0/proxy.conf


/etc/init.d/freeradius start
tail -f /var/log/freeradius/radius.log
