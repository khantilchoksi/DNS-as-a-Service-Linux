# DNS-as-a-service
FROM centos:centos7
RUN yum -y install bind-utils bind && \
    yum clean all

ADD bind-config /

# set up the BIND env and gen rndc key
RUN rndc-confgen -a -c /etc/rndc.key && \
    chown named:named /etc/rndc.key && \
    chmod 755 /entrypoint

# Install IP-UTILS
RUN yum -y update && \
    yum install -y net-tools && \
    yum install -y iputils && \
    yum install -y iproute && \
    yum install -y dhclient && \
    yum clean all

EXPOSE 53/udp 53/tcp

# For configuring OPEN-SSH
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in ; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done);
RUN rm -rf /lib/systemd/system/multi-user.target.wants/;
RUN rm -rf /etc/systemd/system/.wants/;
RUN rm -rf /lib/systemd/system/local-fs.target.wants/;
RUN rm -rf /lib/systemd/system/sockets.target.wants/udev;
RUN rm -rf /lib/systemd/system/sockets.target.wants/initctl;
RUN rm -rf /lib/systemd/system/basic.target.wants/;
RUN rm -rf /lib/systemd/system/anaconda.target.wants/*;
RUN yum install -y openssh-server
VOLUME [ "/sys/fs/cgroup"]

# VOLUME [ "/named" ]
ENTRYPOINT [ "/entrypoint"]
CMD [ "/usr/sbin/named" ]
