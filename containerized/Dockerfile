# DNS-as-a-service
FROM centos:centos7
RUN yum -y install bind-utils bind && \
    yum clean all

ADD bind-config /

# set up the BIND env and gen rndc key
RUN rndc-confgen -a -c /etc/rndc.key && \
    chown named:named /etc/rndc.key && \
    chmod 755 /entrypoint

EXPOSE 53/udp 53/tcp


# VOLUME [ "/named" ]
ENTRYPOINT [ "/entrypoint"]
CMD [ "/usr/sbin/named" ]
