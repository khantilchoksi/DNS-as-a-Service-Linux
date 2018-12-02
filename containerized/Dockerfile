# DNS-as-a-service
FROM centos:centos7

# install bind utils packages:
RUN yum -y install bind-utils bind && \
    yum clean all

ADD bind-config /

# set up the BIND env and gen rndc key
RUN rndc-confgen -a -c /etc/rndc.key && \
    chown named:named /etc/rndc.key && \
    chmod 755 /entrypoint

EXPOSE 53/udp 53/tcp

# Labels consumed by Nulecule Specification
# Volumes:
#  * /named   - this is where all the named data lives
# LABEL io.projectatomic.nulecule.volume.data="/named,128Mi"
# VOLUME [ "/named" ]

# start named services
CMD [ "/usr/sbin/named" ]
