FROM ubuntu:latest
RUN apt update && apt upgrade -y
RUN apt install freeradius freeradius-ldap eapoltest nano -y
COPY raddb /etc/freeradius/3.0
ENTRYPOINT ["sh", "/etc/freeradius/3.0/start.sh"]
