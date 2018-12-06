#!/bin/bash

sed 's/#PermitRootLogin/PermitRootLogin/' < /etc/ssh/sshd_config > /etc/ssh/sshd_config
systemctl restart sshd
passwd
root
root
