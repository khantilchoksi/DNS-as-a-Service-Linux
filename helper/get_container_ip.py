import os
import sys
container_name=sys.argv[1]
a=str(os.system("docker exec -it " +container_name+ " /sbin/ifconfig " + container_name + "vif1 | grep 'inet' | cut -d: -f2 | awk '{print $2}'"))
