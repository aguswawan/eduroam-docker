#!/bin/bash
chown -R freerad:freerad /etc/freeradius/3.0
/etc/init.d/freeradius start
tail -f /var/log/freeradius/radius.log
