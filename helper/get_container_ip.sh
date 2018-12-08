#!/bin/bash
docker exec -it $0 /sbin/ifconfig $0vif1 | grep 'inet' | cut -d: -f2 | awk '{print $2}'
